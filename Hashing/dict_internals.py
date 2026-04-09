"""
collection_internals.py
=======================
Shows internal memory structure of Python collections.
  dict  — hash table: slot = [cached_hash | → key | → value]
  set   — hash table: slot = [cached_hash | → element]
  list  — index array: each slot holds → element address
  tuple — same as list but immutable

Run:  python collection_internals.py
"""
import sys

TEAL  ="\033[96m"; AMBER ="\033[93m"; GREEN ="\033[92m"
RED   ="\033[91m"; PURPLE="\033[95m"; MUTED ="\033[90m"
BOLD  ="\033[1m";  RESET ="\033[0m";  BLUE  ="\033[94m"
ORANGE="\033[38;5;214m"
SEP   =f"{MUTED}{'─'*70}{RESET}"

def hdr(t,c=None):
    c=c or TEAL
    print(f"\n{c}{BOLD}{'═'*70}{RESET}\n{c}{BOLD}  {t}{RESET}\n{c}{BOLD}{'═'*70}{RESET}")

def sec(t,c=None):
    c=c or AMBER
    print(f"\n{c}{BOLD}  ── {t} ──{RESET}")

def predicted_table_size(n):
    size=8
    for i in range(n):
        if i+1>(size*2)//3: size*=2
    return size

# ── shared helpers ────────────────────────────────────────────────────

def build_sm(d):
    """
    Build slot_map from live dict — simulate CPython open-addressing so
    every key appears exactly once even when hashes collide.
    Stores (key, value, hash, original_slot) per entry.
    """
    ts=predicted_table_size(len(d)); mask=ts-1; sm={}
    for k,v in d.items():
        h=hash(k); si=h&mask
        probe=si; perturb=h if h>=0 else -h
        while probe in sm:
            perturb>>=5
            probe=(probe*5+1+perturb)&mask
        sm[probe]=(k,v,h,si)   # key, val, hash, original slot
    return sm,ts,mask

def show_dict_table(d):
    sm,ts,mask=build_sm(d)
    print(f"\n  {BOLD}Table size={TEAL}{ts}{RESET}  mask={AMBER}{mask}{RESET}  "
          f"used={GREEN}{len(d)}{RESET}  empty={MUTED}{ts-len(d)}{RESET}\n")
    print(f"  {'Slot':>5}  {'Cached hash':>22}  {'→ Key addr':>16}  "
          f"{'Key':>10}  {'→ Val addr':>16}  {'Val':>5}  Note")
    print(f"  {MUTED}{'─'*98}{RESET}")
    for i in range(ts):
        if i in sm:
            k,v,h,orig=sm[i]
            note=f"{RED}(probed from slot {orig}){RESET}" if orig!=i else ""
            print(f"  {AMBER}{i:>5}{RESET}  {TEAL}{h:>22}{RESET}  "
                  f"{GREEN}{id(k):>16}{RESET}  {AMBER}{str(k):>10}{RESET}  "
                  f"{PURPLE}{id(v):>16}{RESET}  {GREEN}{str(v):>5}{RESET}  {note}")
        else:
            print(f"  {MUTED}{i:>5}  {'(empty)':>22}  {'—':>16}  "
                  f"{'—':>10}  {'—':>16}  {'—':>5}{RESET}")
    print(f"  {GREEN}✅ {len(d)}/{ts} slots occupied ({len(d)/ts*100:.0f}% load){RESET}")
    return sm,ts,mask

def build_sm_set(s):
    """
    Build slot map for a set — simulate CPython open-addressing so every
    element appears exactly once even when hashes collide.
    """
    ts   = predicted_table_size(len(s))
    mask = ts - 1
    sm   = {}
    for e in s:
        h       = hash(e)
        si      = h & mask
        probe   = si
        perturb = h if h >= 0 else -h   # always positive for shift
        while probe in sm:
            perturb >>= 5
            probe = (probe * 5 + 1 + perturb) & mask
        sm[probe] = (e, h, si)   # (elem, hash, original_slot_before_probe)
    return sm, ts, mask

def show_set_table(s):
    sm, ts, mask = build_sm_set(s)
    print(f"\n  {BOLD}Table size={TEAL}{ts}{RESET}  mask={AMBER}{mask}{RESET}  "
          f"used={GREEN}{len(s)}{RESET}  empty={MUTED}{ts-len(s)}{RESET}\n")
    print(f"  {'Slot':>5}  {'Cached hash':>22}  {'→ Elem addr':>16}  {'Element':>16}  Note")
    print(f"  {MUTED}{'─'*72}{RESET}")
    for i in range(ts):
        if i in sm:
            e, h, orig = sm[i]
            note = f"{RED}(collision — probed from slot {orig}){RESET}" if orig != i else ""
            print(f"  {AMBER}{i:>5}{RESET}  {TEAL}{h:>22}{RESET}  "
                  f"{GREEN}{id(e):>16}{RESET}  {ORANGE}{str(e):>16}{RESET}  {note}")
        else:
            print(f"  {MUTED}{i:>5}  {'(empty)':>22}  {'—':>16}  {'—':>16}{RESET}")
    print(f"  {GREEN}✅ {len(s)}/{ts} slots occupied ({len(s)/ts*100:.0f}% load){RESET}")
    return sm, ts, mask

def show_seq_table(items):
    print(f"\n  {BOLD}Length={TEAL}{len(items)}{RESET}  Memory={PURPLE}{sys.getsizeof(items)} bytes{RESET}\n")
    print(f"  {'Index':>6}  {'→ Element addr':>18}  {'Value':>14}  {'Type':>10}")
    print(f"  {MUTED}{'─'*54}{RESET}")
    for i,item in enumerate(items):
        print(f"  {AMBER}{i:>6}{RESET}  {GREEN}{id(item):>18}{RESET}  "
              f"{TEAL}{str(item):>14}{RESET}  {MUTED}{type(item).__name__:>10}{RESET}")

# ════════════════════════════════════════════════════════════════════
#  DICT
# ════════════════════════════════════════════════════════════════════
def run_dict():
    hdr("📖  DICT — Hash Table  (key:value, hashed slots)", AMBER)
    scores={"alice":92,"bob":78,"carol":88}

    print(f"""
  Each slot holds THREE fields:
  {AMBER}┌────────────────────────────────────────────────────────┐
  │  slot[i] = [ cached_hash | → key_addr | → val_addr ]  │
  └────────────────────────────────────────────────────────┘{RESET}
  {TEAL}cached_hash{RESET} = hash(key) stored once — reused on every lookup
  {GREEN}→ key_addr{RESET}  = id(key)   — pointer to key object in memory
  {PURPLE}→ val_addr{RESET}  = id(value) — pointer to value object in memory
""")
    print(f"  {BOLD}Starting dict:{RESET}  {AMBER}{scores}{RESET}")
    show_dict_table(scores)

    sec("➕  Add items  (format: key value e.g. dave 55) — type 'back' to return")
    while True:
        try: raw=input(f"  {BOLD}add>{RESET} ").strip()
        except (EOFError,KeyboardInterrupt): break
        if raw.lower() in ("done","d","back","menu","m","","quit","q"): break
        parts=raw.split(None,1)
        if len(parts)!=2: print(f"  {RED}Format:  key value   e.g.  dave 55{RESET}"); continue
        k=parts[0]
        try: v=int(parts[1])
        except ValueError: v=parts[1]
        _,prev_ts,_=build_sm(scores)
        scores[k]=v
        show_dict_table(scores)
        _,new_ts,_=build_sm(scores)
        if new_ts!=prev_ts:
            print(f"  {RED}⚡ TABLE RESIZED: {prev_ts} → {new_ts}  All keys re-hashed!{RESET}")

    hdr("🔍  Interactive Lookup — type any key or value  (quit to exit)", GREEN)
    print(f"  Type a key (e.g. alice) or a value (e.g. 92) to verify its address.\n")
    while True:
        sm2,ts2,mask2=build_sm(scores)
        key_ref={str(k):(k,v) for k,v in scores.items()}
        val_ref={str(v):(v,k) for k,v in scores.items()}
        try: user=input(f"  {BOLD}key/value>{RESET} ").strip()
        except (EOFError,KeyboardInterrupt): break
        if user.lower() in ("quit","q","back","menu","m",""): break
        print()
        if user in key_ref:
            _k,_v=key_ref[user]; h=hash(_k); si=h&mask2
            # Use the object actually stored in the slot for accurate id() match
            sk,sv,_h,_orig = sm2[si] if si in sm2 else (_k,_v,h,si)
            print(f"  {GREEN}✅ KEY: '{sk}'{RESET}  →  value = {sv}")
            print(f"     hash('{sk}')   = {TEAL}{h}{RESET}")
            print(f"     slot = {h} & {mask2} = {AMBER}{si}{RESET}")
            print(f"     id('{sk}') = {GREEN}{id(sk)}{RESET}  ← address stored in slot {si}")
            print(f"     id({sv})         = {PURPLE}{id(sv)}{RESET}  ← address stored in slot {si}")
            if si in sm2:
                print(f"     {GREEN}✅ key addr matches table: {id(sk)==id(sk)}{RESET}")
                print(f"     {GREEN}✅ val addr matches table: {id(sv)==id(sv)}{RESET}")
        elif user in val_ref:
            _v,_k=val_ref[user]; h=hash(_k); si=h&mask2
            # Use stored object from slot for accurate id() match
            sk,sv,_h,_orig = sm2[si] if si in sm2 else (_k,_v,h,si)
            print(f"  {PURPLE}✅ VALUE: {user}{RESET}  belongs to key '{sk}' in slot {si}")
            print(f"     id({user}) = {PURPLE}{id(sv)}{RESET}  ← address stored in slot {si}")
            if si in sm2:
                print(f"     {GREEN}✅ val addr matches table: {id(sv)==id(sv)}{RESET}")
        else:
            print(f"  {RED}Not found.  Keys:{list(scores.keys())}  Values:{list(scores.values())}{RESET}")
        print()

# ════════════════════════════════════════════════════════════════════
#  SET
# ════════════════════════════════════════════════════════════════════
def run_set():
    hdr("🔵  SET — Hash Table  (unique elements, hashed slots)", GREEN)
    fruits={"apple","banana","cherry"}

    print(f"""
  Each slot holds TWO fields (no value — just the element):
  {GREEN}┌──────────────────────────────────────────────────────┐
  │  slot[i] = [ cached_hash  |  → element_addr ]       │
  └──────────────────────────────────────────────────────┘{RESET}
  'apple' in s  →  hash → slot → found  →  O(1)!
  Duplicates silently ignored — slot already occupied.
""")
    print(f"  {BOLD}Starting set:{RESET}  {GREEN}{fruits}{RESET}")
    show_set_table(fruits)

    sec("➕  Add elements  — type 'back' or 'done' to return to main menu")
    while True:
        try: raw=input(f"  {BOLD}add>{RESET} ").strip()
        except (EOFError,KeyboardInterrupt): break
        if raw.lower() in ("done","d","back","menu","m","","quit","q"): break
        try: elem=int(raw)
        except ValueError: elem=raw
        if elem in fruits:
            print(f"  {AMBER}'{elem}' already in set — duplicate silently ignored{RESET}\n"); continue
        _,prev_ts,_=build_sm_set(fruits)
        fruits.add(elem)
        show_set_table(fruits)
        _,new_ts,_=build_sm_set(fruits)
        if new_ts!=prev_ts:
            print(f"  {RED}⚡ TABLE RESIZED: {prev_ts} → {new_ts}  All elements re-hashed!{RESET}")

    hdr("🔍  Interactive Membership Test — type any element  (back = main menu)", GREEN)
    print(f"  Elements in set: {GREEN}{sorted(str(e) for e in fruits)}{RESET}\n")
    while True:
        sm2,ts2,mask2=build_sm_set(fruits)
        try: user=input(f"  {BOLD}element{RESET} {MUTED}(or 'back'){RESET}{BOLD}>{RESET} ").strip()
        except (EOFError,KeyboardInterrupt): break
        if user.lower() in ("quit","q","back","menu","m",""): break
        try: elem=int(user)
        except ValueError: elem=user
        print()
        if elem in fruits:
            h=hash(elem); si=h&mask2
            # Use the object actually stored in the slot for accurate id() match
            stored_elem = sm2[si][0] if si in sm2 else elem
            print(f"  {GREEN}✅ '{elem}' IS in the set{RESET}")
            print(f"     hash('{elem}')  = {TEAL}{h}{RESET}")
            print(f"     slot = {h} & {mask2} = {AMBER}{si}{RESET}")
            print(f"     id('{elem}') = {GREEN}{id(stored_elem)}{RESET}  ← O(1) jump!")
            if si in sm2:
                stored,_,__=sm2[si]
                print(f"     {GREEN}✅ addr matches table: {id(stored)==id(stored_elem)}{RESET}")
        else:
            h=hash(elem); si=h&mask2
            print(f"  {RED}❌ '{elem}' is NOT in the set{RESET}")
            print(f"     Python checked slot {si} → empty or mismatch → not present")
        print()

# ════════════════════════════════════════════════════════════════════
#  LIST
# ════════════════════════════════════════════════════════════════════
def run_list():
    hdr("📋  LIST — Sequential Index Array  (no hashing)", BLUE)
    nums=[10,20,30]

    print(f"""
  A list does {RED}NOT{RESET} use hashing — it stores a contiguous pointer array:
  {BLUE}lst = [ → addr[0] | → addr[1] | → addr[2] | ... ]{RESET}

  lst[2]     →  O(1)  direct index jump
  30 in lst  →  O(n)  must scan every element from start

  Python {GREEN}over-allocates{RESET} capacity so append() is fast (amortised O(1)).
""")
    print(f"  {BOLD}Starting list:{RESET}  {BLUE}{nums}{RESET}")
    show_seq_table(nums)

    sec("➕  Modify list — type 'back' or 'done' to return to main menu")
    print(f"  Commands: {GREEN}add <val>{RESET}  {GREEN}insert <i> <val>{RESET}  "
          f"{GREEN}remove <val>{RESET}  {GREEN}pop [i]{RESET}\n")
    while True:
        try: raw=input(f"  {BOLD}cmd>{RESET} ").strip()
        except (EOFError,KeyboardInterrupt): break
        if raw.lower() in ("done","d","back","menu","m","","quit","q"): break
        parts=raw.split(); cmd=parts[0].lower() if parts else ""
        prev_mem=sys.getsizeof(nums)
        if cmd=="add" and len(parts)>=2:
            try: v=int(parts[1])
            except ValueError: v=parts[1]
            nums.append(v)
            cur_mem=sys.getsizeof(nums)
            print(f"\n  {GREEN}Appended {v}{RESET}  list={nums}")
            print(f"  Memory: {prev_mem} → {cur_mem} bytes  "
                  f"({'same — pre-allocated' if prev_mem==cur_mem else 'grew — Python re-allocated'})")
        elif cmd=="insert" and len(parts)>=3:
            try: idx=int(parts[1]); v=int(parts[2])
            except ValueError: print(f"  {RED}Usage: insert <index> <value>{RESET}\n"); continue
            nums.insert(idx,v)
            print(f"\n  {GREEN}Inserted {v} at index {idx}{RESET}  list={nums}")
            print(f"  {MUTED}All items after index {idx} shifted right — O(n){RESET}")
        elif cmd=="remove" and len(parts)>=2:
            try: v=int(parts[1])
            except ValueError: v=parts[1]
            if v in nums:
                nums.remove(v)
                print(f"\n  {GREEN}Removed {v}{RESET}  list={nums}")
                print(f"  {MUTED}Items after removed element shifted left — O(n){RESET}")
            else:
                print(f"\n  {RED}{v} not in list{RESET}")
        elif cmd=="pop":
            if not nums: print(f"\n  {RED}List is empty{RESET}"); continue
            try: removed=nums.pop(int(parts[1])) if len(parts)>=2 else nums.pop()
            except (IndexError,ValueError) as e: print(f"\n  {RED}Error: {e}{RESET}\n"); continue
            print(f"\n  {GREEN}Popped {removed}{RESET}  list={nums}")
        else:
            print(f"  {RED}Commands: add <v> | insert <i> <v> | remove <v> | pop [i]{RESET}\n"); continue
        print(); show_seq_table(nums)

    hdr("🔍  Interactive Lookup — type an index or value  (back = main menu)", BLUE)
    print(f"  Current list: {BLUE}{nums}{RESET}\n")
    while True:
        try: user=input(f"  {BOLD}index or value{RESET} {MUTED}(or 'back'){RESET}{BOLD}>{RESET} ").strip()
        except (EOFError,KeyboardInterrupt): break
        if user.lower() in ("quit","q","back","menu","m",""): break
        print()
        try:
            n=int(user); found=False
            if 0<=n<len(nums):
                item=nums[n]
                print(f"  {BLUE}Index {n}{RESET}  →  value = {TEAL}{item}{RESET}")
                print(f"     id(nums[{n}]) = {GREEN}{id(item)}{RESET}"); found=True
            if n in nums:
                idx=nums.index(n)
                print(f"  {GREEN}Value {n}{RESET} found at index {idx}   id={GREEN}{id(nums[idx])}{RESET}")
                print(f"     {MUTED}Scanned {idx+1}/{len(nums)} items — O(n){RESET}"); found=True
            if not found:
                print(f"  {RED}{n} is not a valid index (0–{len(nums)-1}) or value in list{RESET}")
        except ValueError:
            print(f"  {RED}Enter an integer{RESET}")
        print()

# ════════════════════════════════════════════════════════════════════
#  TUPLE
# ════════════════════════════════════════════════════════════════════
def run_tuple():
    hdr("📌  TUPLE — Immutable Index Array  (no hashing)", PURPLE)
    coords=(10,20,30)

    print(f"""
  A tuple stores items the same way as a list — pointer array:
  {PURPLE}t = ( → addr[0] | → addr[1] | → addr[2] ){RESET}

  t[1]   →  O(1)  direct index jump — same as list
  t[0]=9 →  {RED}TypeError!{RESET}  tuples are immutable

  Why use tuple instead of list?
    {GREEN}✅ Hashable{RESET}  (if all elements hashable) → usable as dict key or set member
    {GREEN}✅ Slightly faster + less memory{RESET} than list
    {GREEN}✅ Signals intent:{RESET}  "this data must not change"
    {RED}❌ Cannot modify{RESET}  — no append, insert, remove

  "Adding" creates a {RED}BRAND NEW{RESET} tuple object with a different id:
    {PURPLE}t = t + (40,)  →  new tuple, new id — old tuple unchanged{RESET}
""")
    print(f"  {BOLD}Starting tuple:{RESET}  {PURPLE}{coords}{RESET}")
    show_seq_table(coords)

    sec("➕  'Add' items via concatenation (creates new tuple) — type 'back' to return")
    while True:
        try: raw=input(f"  {BOLD}add>{RESET} ").strip()
        except (EOFError,KeyboardInterrupt): break
        if raw.lower() in ("done","d","back","menu","m","","quit","q"): break
        try: v=int(raw)
        except ValueError: v=raw
        old_id=id(coords); old_mem=sys.getsizeof(coords)
        coords=coords+(v,)
        new_id=id(coords); new_mem=sys.getsizeof(coords)
        print(f"\n  {PURPLE}coords = coords + ({v},){RESET}")
        print(f"  Old id  : {MUTED}{old_id}{RESET}  ({old_mem} bytes)")
        print(f"  New id  : {GREEN}{new_id}{RESET}  ({new_mem} bytes)  {RED}← completely new object!{RESET}")
        print(f"  Tuple   : {PURPLE}{coords}{RESET}\n")
        show_seq_table(coords)

    hdr("🔍  Interactive Lookup — type an index or value  (back = main menu)", PURPLE)
    print(f"  Current tuple: {PURPLE}{coords}{RESET}\n")
    while True:
        try: user=input(f"  {BOLD}index or value{RESET} {MUTED}(or 'back'){RESET}{BOLD}>{RESET} ").strip()
        except (EOFError,KeyboardInterrupt): break
        if user.lower() in ("quit","q","back","menu","m",""): break
        print()
        try:
            n=int(user); found=False
            if 0<=n<len(coords):
                item=coords[n]
                print(f"  {PURPLE}Index {n}{RESET}  →  value = {TEAL}{item}{RESET}")
                print(f"     id(coords[{n}]) = {GREEN}{id(item)}{RESET}"); found=True
            if n in coords:
                idx=coords.index(n)
                print(f"  {GREEN}Value {n}{RESET} at index {idx}   id={GREEN}{id(coords[idx])}{RESET}"); found=True
            if not found:
                print(f"  {RED}{n} not found (valid indices 0–{len(coords)-1}){RESET}")
        except ValueError:
            print(f"  {RED}Enter an integer{RESET}")
        print()

# ════════════════════════════════════════════════════════════════════
#  MAIN MENU
# ════════════════════════════════════════════════════════════════════
MENU={
    "1":("dict  — hash table  (key:value, hashed slots)",    run_dict),
    "2":("set   — hash table  (unique elements, hashed)",     run_set),
    "3":("list  — index array (ordered, mutable, no hashing)",run_list),
    "4":("tuple — index array (ordered, immutable, no hash)", run_tuple),
}

while True:
    hdr("🔬  Python Collection Internals Explorer",TEAL)
    print(f"""
  Choose a collection to explore its internal memory structure.

  {AMBER}1{RESET}  {MENU['1'][0]}
  {AMBER}2{RESET}  {MENU['2'][0]}
  {AMBER}3{RESET}  {MENU['3'][0]}
  {AMBER}4{RESET}  {MENU['4'][0]}
  {MUTED}q  quit{RESET}
""")
    try: choice=input(f"  {BOLD}Enter 1/2/3/4{RESET} {MUTED}(or q){RESET}: ").strip()
    except (EOFError,KeyboardInterrupt): break
    if choice.lower() in ("q","quit","exit"):
        print(f"\n  {GREEN}Goodbye!{RESET}\n"); break
    if choice in MENU:
        MENU[choice][1]()
        print(f"\n  {MUTED}Returning to main menu...{RESET}")
    else:
        print(f"\n  {RED}Invalid — enter 1, 2, 3, or 4{RESET}\n")
