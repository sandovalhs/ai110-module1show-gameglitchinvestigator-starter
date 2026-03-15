# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

- I noticed that the new game button was not working.  I expected it to start a new game and allow me to guess for a different number, but when it was clicked it would not start a new game and it would say something like "you already won, start a new game"

- I also noticed that the hints were backwards. When I would guess something higher, it would tell me to go higher.  Guessing lower than the target would tell me to go lower.  I expected it to tell me the oppsoite in both situations because this was misleading

- Another bug I noticed is that it allowed me to guess out of the specified number range.  I expected the program to tell me "guess out of range" when I guessed out of range but instead it accepted the guess and took away an attempt which was clearly wrong.

- I also noticed that the game does not correctly implement difficulty, as the range of guesses never changes.  I expected the range to update based on difficulty but it always stayed from 0-100.

-

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? I used Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- The ai correctly identified two bugs when I asked it to explain how the difficulty changed in the game.  It also correctly identified the bug about going higher or lower.  To verify this I made sure it passed all the test cases as there were some failures with the generated cases.
I debugged the failures by reviewing what they tested.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
The Ai frequently tried to delete my comments whihc became frustrating.
I understand it was trying to clean up my code as it refactored but its odd that it tries to delete a lot of my comments without knowing their contents anyway.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I made sure to agree with all the test cases and verified that they were checkign for correctness.  If they passed then I would know the code works, so when failures would happen I would investigate and debug.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
The difficulty range was messed up and some test cases were failing, to fix this I asked the ai to updatye the ranges according to my specific ranges that i wanted and then we started passing them again.
- Did AI help you design or understand any tests? How?
Yes, I asked if it agreed with the problem I indentified and it helped me come up with a fix.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
