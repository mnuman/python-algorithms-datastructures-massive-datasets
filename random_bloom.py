import random
import time
from bloom import BloomFilter


print("Generating entries")

entries = set()
while len(entries) != 1_000_000:
    entries.add(str(random.randint(0, 10**12)))


bf = BloomFilter(10**7, 0.02)
print(f"Generated entries: {len(entries)}")
print("Subsetting entries")
existing_entries = {i for i in list(entries)[: 10**6]}
print("Adding entries to Bloom filter")
for i in existing_entries:
    bf.insert(i)

non_existing_entries = {
    str(int(i) + 1)
    for i in list(existing_entries)[: 10**6]
    if str(int(i) + 1) not in existing_entries
}

print(f"Started with non_existing_entries: {len(non_existing_entries)}")
while len(non_existing_entries) < 10**6:
    i = str(random.randint(0, 10**12))
    if i not in non_existing_entries and i not in existing_entries:
        non_existing_entries.add(i)
    if len(non_existing_entries) % 100000 == 0:
        print(f"Generated {len(non_existing_entries)}")

existing = 0
non_existing = 0

start = time.time()
for i in existing_entries:
    existing += 1 if bf.lookup(i) else 0
intermediate = time.time()
for i in non_existing_entries:
    non_existing += 1 if bf.lookup(i) else 0
end = time.time()
print(f"Existing - duration: {intermediate - start}")
print(f"Existing - found:    {existing/ 1_000_000}")

print(f"Non-existing - duration: {end - intermediate}")
print(f"Non-existing - found:    {non_existing / 1_000_000}")
