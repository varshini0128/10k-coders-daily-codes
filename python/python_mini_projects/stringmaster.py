import random

sentences = [
    "python is amazing",
    "coding improves thinking",
    "practice makes perfect",
    "string methods are powerful",
    "mini projects are fun"
]

print("\n🎮 WELCOME TO STRING MASTER CHALLENGE 🎮")
print("---------------------------------------")

score = 0

# pick random sentence
sentence = random.choice(sentences)

print("\nYour base sentence is:")
print(f"👉 {sentence}")

print("\nComplete all 10 tasks!\n")

# ------------------ Level 1: LOWER ------------------
ans = input("1) Type the sentence in LOWERCASE: ").strip()
if ans == sentence.lower():
    score += 1
    print("✔ Correct")
else:
    print("❌ Wrong")

# ------------------ Level 2: UPPER ------------------
ans = input("\n2) Type the sentence in UPPERCASE: ").strip()
if ans == sentence.upper():
    score += 1
    print("✔ Correct")
else:
    print("❌ Wrong")

# ------------------ Level 3: TITLE ------------------
ans = input("\n3) Type the sentence in Title Case: ").strip()
if ans == sentence.title():
    score += 1
    print("✔ Correct")
else:
    print("❌ Wrong")

# ------------------ Level 4: CAPITALIZE ------------------
ans = input("\n4) Capitalize only first letter: ").strip()
if ans == sentence.capitalize():
    score += 1
    print("✔ Correct")
else:
    print("❌ Wrong")

# ------------------ Level 5: COUNT ------------------
char = "a"
print(f"\n5) How many times does '{char}' appear?")
ans = input("Count: ").strip()
if ans.isdigit() and int(ans) == sentence.count(char):
    score += 1
    print("✔ Correct")
else:
    print("❌ Wrong")

# ------------------ Level 6: FIND ------------------
print("\n6) What is the FIRST position of letter 'i'?")
ans = input("Enter index: ").strip()
if ans.isdigit() and int(ans) == sentence.find("i"):
    score += 1
    print("✔ Correct")
else:
    print("❌ Wrong")

# ------------------ Level 7: RFIND ------------------
print("\n7) What is the LAST position of letter 'i'?")
ans = input("Enter index: ").strip()
if ans.isdigit() and int(ans) == sentence.rfind("i"):
    score += 1
    print("✔ Correct")
else:
    print("❌ Wrong")
    
# ------------------ Level 8: REPLACE (dynamic and always valid) ------------------
word_to_replace = random.choice(sentence.split())   # choose valid word from sentence

print(f"\n8) Replace the word '{word_to_replace}' with 'XYZ'")
correct_sentence = sentence.replace(word_to_replace, "XYZ")

ans = input("Enter new sentence: ").strip()

if ans == correct_sentence:
    score += 1
    print("✔ Correct")
else:
    print("❌ Wrong")
    print("Correct answer:", correct_sentence)

# ------------------ Level 9: SPLIT & JOIN ------------------
print("\n9) Join the words using '-' (hyphens)")
joined_version = "-".join(sentence.split())  # split + join
ans = input("Enter joined sentence: ").strip()
if ans == joined_version:
    score += 1
    print("✔ Correct")
else:
    print("❌ Wrong")

# ------------------ Level 10: STARTSWITH / ENDSWITH ------------------
print("\n10) LAST LEVEL: Two questions")

start = input("Does the sentence START with 'p'? (yes/no): ").strip().lower()
end = input("Does it END with 'g'? (yes/no): ").strip().lower()

start_correct = sentence.startswith("p")
end_correct = sentence.endswith("g")

start_ans = (start == "yes" and start_correct) or (start == "no" and not start_correct)
end_ans = (end == "yes" and end_correct) or (end == "no" and not end_correct)

if start_ans and end_ans:
    score += 1
    print("✔ Correct")
else:
    print("❌ Wrong")

# ------------------ END ------------------

print("\n---------------------------------------")
print(f"🎉 Your Final Score: {score}/10")

if score == 10:
    print("🏆 STRING MASTER! Perfect score!")
elif score >= 7:
    print("🔥 Excellent! You know your string methods.")
else:
    print("🙂 Keep practicing, you’ll get better!")
