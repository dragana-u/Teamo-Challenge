# Teamo-Challenge
My take on the ML and Data analytics challenge from TeamLift </br>
<hr>

## Technical Part
### Task 1: ER Diagram
Teamo AI compares user-submitted skill names to an administrator's list using various matching methods, returning results based on internal scores. </br>
The task includes drawing an ER diagram to design the database structure for Teamo AI, with entities such as User, Administrator, Skill, Query, and MatchResult, ensuring to store matching methods and scores, and defining relationships between these entities.

### Task 2: Python script
This task consists of two scripts for Teamo: one using BERT for advanced skill matching and another without BERT for better performance on limited memory environments.

BERT Version: The script that includes the BERT model leverages its powerful contextual embeddings to compute skill matches. However, due to BERT’s high memory requirements, this version exceeds the memory limits of Render’s free tier, which is why it’s not hosted on the live platform. </br>

Non-BERT Version: To accommodate these limitations, the script without BERT uses simpler algorithms like Levenshtein Distance and Jaccard Similarity to match skills. This version has been deployed on Render and is available for use on GitHub pages: https://dragana-u.github.io/Teamo-Challenge/ </br>

If you want to test the BERT version locally, you can do so using the following curl command in your terminal: </br>
```curl -X POST "http://127.0.0.1:5000/match" -H "Content-Type: application/json" -d '{"skill": "nlp"}'``` </br>

Replace "nlp" with the skill you want to test. This command will send a POST request to your local server and receive the skill matches in response. </br>

## Creative part
### Task 3: Using Teamo to enhance your workflow

After exploring a lot of AI tools I had never seen before, I was mostly drawn to Gamma. I used Gamma to create a presentation specifically for this challenge and was impressed by the results. You can view the presentation here, it is labeled gamma-presentation. </br>
Finally, I gave my review to the product and an idea for brainstorming. </br>

### Final thoughts
I enjoyed working on this challenge and exploring new tools, as well as using the ones I was already familiar with. ChatGPT and GitHub copilot were my go-to for doing this challenge, specifically by asking them to brainstorm with me. A prompt I love to use is: My task is [], can you help me brainstorm ideas to help me tackle this problem? And it always works like a charm!</br>
