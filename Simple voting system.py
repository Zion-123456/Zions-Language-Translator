votes = {}
candidates = ["Alice", "Bob", "Charlie"]
candidates_initials = ["A", "B", "C"]

print("Candidates:", candidates)

while True:
    vote = input("Vote for a candidate (or 'end' to finish): ")
    if vote.lower() == 'end':
        break
    if vote in candidates_initials:
        if vote in votes:
            votes[vote] += 1
        else:
            votes[vote] = 1
    else:
        print("Invalid candidate.")

print("\nVoting Results:")
for candidate, count in votes.items():
    print(f"{candidate}: {count} vote(s)")

    #Testing Git commit