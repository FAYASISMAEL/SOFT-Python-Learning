# Given set
it_companies = {
    "Facebook",
    "Google",
    "Microsoft",
    "Apple",
    "IBM",
    "Oracle",
    "Amazon"
}


# 1. Find the length of the set
print("Number of IT companies:", len(it_companies))


# 2. Add 'Twitter' to it_companies
it_companies.add("Twitter")
print("After adding Twitter:", it_companies)


# 3. Insert multiple IT companies at once
it_companies.update(["Netflix", "Tesla", "Adobe"])

print("After adding multiple companies:", it_companies)


# 4. Remove one company from the set
it_companies.remove("IBM")

print("After removing IBM:", it_companies)


# 5. Difference between remove() and discard()

# remove()
companies = {"Google", "Apple"}

companies.remove("Microsoft")
# KeyError because Microsoft is not in the set
# Gives an error if the item does not exist

# discard()
companies = {"Google", "Apple"}

companies.discard("Microsoft")
# No error
# Does not give an error if the item does not exist