# AI for Teaching, Learning and Collaborating --- Workshop Script

**D-Lab AI Pulse | ~50 minutes**

---

## SLIDE 1: Title Slide
**[0:00 -- 0:30]**

Welcome everyone to today's AI Pulse workshop. My name is [name], and I'm with D-Lab at UC Berkeley.

Today we're going to look at how AI tools can help with three things that take up most of our time in academia: teaching, learning, and collaborating. We'll do live demos throughout, so you'll see these tools in action.

Let's start with the problem.

---

## SLIDE 2: The Bottleneck: Learning
**[0:30 -- 2:30]**

Think about the traditional classroom. There's one instructor and dozens of students, and teaching happens "by the average." Material is presented at a pace and a level that's meant to work for most people. But what does that actually mean in practice?

It means a student gets stuck on a concept --- maybe it's a proof, maybe it's a programming technique, maybe it's a statistical method --- and the next office hours are five days away. So they either spin their wheels trying to figure it out alone, or they move on without really understanding, and the gap compounds.

And if you've ever read course evaluations, you know the split: half the class says "this course moved too fast" and the other half says "this course was too slow." The instructor literally cannot win, because they're teaching to the average and the average student doesn't exist.

Here's another one that hits graduate students hard. You get excited about a research idea. You spend weeks reading dozens of papers, building up the literature, mapping the landscape --- and then you find out your idea was published two years ago. The time investment to learn that your project isn't novel is enormous, and there's currently no shortcut for it.

---

## SLIDE 3: The Bottleneck: Teaching & Collaborating
**[2:30 -- 4:30]**

On the teaching side, instructors spend a disproportionate amount of time on logistics and formatting. Wrestling with LaTeX, preparing problem sets, formatting assignments --- time that could go toward actually improving the syllabus, rethinking how concepts are taught, or advising students. And GSIs --- they answer the same email 30 times a semester. "Where is the rubric?" "Can I submit late?" "How do I request DSP accommodations?" Every semester, the same questions.

And collaboration --- how many of you have left a research group meeting and then realized that people disagree on who's supposed to do what and when it's due? *[Pause for nods.]* It happens constantly. Meeting notes are scattered or incomplete. A team of co-authors has partial results in one Google Doc, a draft in another, data files in email attachments, and lit review notes in Slack. There's no single source of truth.

These are all solvable problems. Let me show you what exists today.

---

## SLIDE 4: A New Paradigm?
**[4:30 -- 5:30]**

What we're looking at is a shift toward personalized education. The idea is simple: students can use AI as a personalized tutor, navigating material at their own pace, getting unstuck immediately instead of waiting for office hours. Meanwhile, instructors are freed from repetitive work and can focus on the things that actually require expertise --- updating the curriculum, advising, designing better assessments.

And for teams, shared AI workspaces can capture decisions, assign tasks, and maintain that single source of truth.

Today we'll cover three main tools: NotebookLM for learning and teaching, Notion AI for writing and team workflows, and Otter AI for meeting transcription and intelligence. We'll also mention Curipod, Mizou, and Mural in passing.

---

## SLIDE 5: Today's Roadmap
**[5:30 -- 6:00]**

Here's the roadmap. First, a deep dive into NotebookLM --- what it is, what it can do, and a concept we're calling the "Bureaucratic Agent." Second, how to use it for learning and research, with a live demo of a literature review workflow. Third, collaboration tools --- Notion AI for writing and project management, Otter AI for meetings. Discussion throughout and at the end.

Let's start with NotebookLM.

---

## SLIDE 6: What is NotebookLM?
**[6:00 -- 8:00]**

NotebookLM is Google's source-grounded AI. It's powered by Gemini, and the key thing that makes it different from ChatGPT or Claude is this: answers come from YOUR documents, not from the internet.

When you use ChatGPT and ask it to summarize a paper, it generates a summary from its training data --- it's predicting what a summary would look like. NotebookLM is different. You upload documents --- papers, lecture notes, syllabi, anything --- and the AI generates content grounded specifically in those sources. Every claim is traceable back to your materials. It doesn't hallucinate because it's not generating from patterns --- it's retrieving from your documents.

It can also now search the web to find new sources and add them to your notebook, so it's not purely limited to what you upload.

It's free. Go to notebooklm.google.com.

---

## SLIDE 7: NotebookLM: What Can It Do?
**[8:00 -- 12:00]**

Let me show you everything NotebookLM can generate from your uploaded sources. I'm going to do a rapid-fire tour --- about 30 seconds each --- so you get a sense of the range.

**[DEMO: Chat with the agent]**

First, the most basic feature. I've uploaded a few papers into this notebook. I can just ask it a question in natural language. "What are the main findings across these papers?" And it answers, with inline citations pointing back to specific passages in the sources. I can click any citation to jump to the exact paragraph.

**[DEMO: Summaries]**

I can ask for a summary of any source, or of all sources combined. It generates a structured summary with key points, all grounded in the actual text.

**[DEMO: Audio Overview]**

This is the one that gets the most attention. NotebookLM generates a conversational audio overview --- it sounds like a podcast with two hosts discussing your material. You can choose the format: deep dive, brief summary, critique, or debate. People listen to these during commutes. It's surprisingly well-produced.

**[DEMO: Mind Maps]**

It can generate a visual mind map of how concepts in your sources connect. Useful for seeing the big picture of a literature.

**[DEMO: Flashcards and Quizzes]**

Flashcards with an "Explain" button when you get something wrong. Quizzes with multiple choice, short answer, or essay questions --- all grounded in your sources. You can generate a new study guide from the questions you missed.

**[DEMO: Slide Decks]**

It can generate slide decks from your content. Useful as a starting point for presentations.

**[DEMO: Sharing]**

And finally, notebooks can be shared. A study group can create a shared notebook with all their readings. A professor can create a notebook and share it as a resource for the class.

---

## SLIDE 8: The "Bureaucratic Agent"
**[12:00 -- 14:30]**

Now here's an idea that I think is one of the most immediately useful applications for anyone who teaches or runs a lab.

Take a course syllabus. Add UC Berkeley's regulations on academic integrity, DSP accommodations, sickness and athletic absence policies, grading policies. Upload them all into one NotebookLM notebook. Now you have a chatbot that can answer any of those questions that GSIs get asked 30 times a semester --- and the answers are grounded in the actual policy documents.

"Can I submit this assignment late?" The bot checks the syllabus and tells them the late policy. "How do I request DSP accommodations?" It walks them through the process from the actual UC Berkeley documentation. "What constitutes academic dishonesty on the final project?" It pulls from the academic integrity policy.

This same idea applies to other settings. Lab safety rules and protocols --- upload the manual, and new lab members can ask questions about it. How to use the EML SLURM server --- upload the documentation. Major and minor requirements --- upload the advising handbook. How enrollment and waitlists work --- upload the registrar's FAQ.

You're creating a grounded Q&A agent that saves everyone time and gives correct, traceable answers.

---

## SLIDE 9: NotebookLM for Research
**[14:30 -- 16:30]**

NotebookLM isn't just for coursework. It's increasingly popular as a research tool.

Andrej Karpathy --- founding member of OpenAI, former head of AI at Tesla --- has talked publicly about how he uses NotebookLM whenever he reads papers. The idea is that you can upload a stack of papers and have a conversation about them: find contradictions, compare methodologies, surface connections you might miss reading one paper at a time.

% TODO: Show Karpathy tweet screenshot here

This is especially valuable in two situations. First, grad students starting a new project. You're entering an unfamiliar literature and you need to quickly build a mental map of who's done what, what the open questions are, and whether your idea is actually novel. Second, researchers joining a new lab or switching fields --- you need to get up to speed on a body of work you didn't grow up with.

Let me show you a workflow for this.

---

## SLIDE 10: Demo: Literature Review Workflow
**[16:30 -- 21:00]**

**[LIVE DEMO]**

Let me walk through how you'd use NotebookLM to start a new research project.

*[Open NotebookLM. Create a new notebook.]*

Step one. I'll paste in a short research idea --- just a paragraph or two describing what I want to investigate, with a few references I already know about.

*[Upload 3-4 papers.]*

Step two. I'll ask NotebookLM: "Based on these papers, how novel is this research idea? What has already been done, and what hasn't?"

*[Show the response. Point out inline citations.]*

This is the question that normally takes weeks of reading to answer. NotebookLM gives you a first-pass answer immediately, with citations. You still need to verify --- this is a starting point, not a final answer --- but it dramatically reduces the time to learn whether your idea has legs.

Step three. I can use the search feature to find more relevant papers and add them to the notebook.

*[Demonstrate adding a source via search.]*

Step four. As I keep adding papers, I can ask for synthesis. "What are the main methodological approaches in this literature?" "How do these three papers disagree?" "What gaps remain?"

*[Show a synthesis query.]*

Step five. I'll generate a mind map to visualize how the concepts connect.

*[Generate and show the mind map.]*

The notebook grows with your project. It becomes a living literature review that you can query at any stage of your research.

This workflow is especially powerful for the grad student problem I mentioned at the start: you can figure out in an afternoon what used to take weeks --- whether your idea is novel, who the key authors are, and where the open questions lie.

---

## SLIDE 11: In Passing: Teaching Tools
**[21:00 -- 22:00]**

Before we move to collaboration, two tools worth knowing about for anyone who teaches.

**Curipod** is an AI-powered interactive lesson builder. You give it your content and it generates polls, word clouds, open-ended prompts --- tools for real-time student engagement during lectures. Think of it as a smart version of iClicker that creates its own questions.

**Mizou** lets you build custom AI tutoring chatbots grounded in your course material. Students interact with the bot for practice, review, and Q&A. It's like creating a customized version of the "Bureaucratic Agent" we discussed, but specifically designed for tutoring.

Both are free to try and specifically designed for educational settings. I'll have the links on the last slide.

---

## SLIDE 12: Collaborating: The Problem
**[22:00 -- 23:00]**

We've seen how NotebookLM helps individuals learn and how teams can share notebooks. But real collaboration involves more than shared documents. You need to write together, track tasks, capture meeting decisions, and keep projects moving.

I should also mention **Mural** --- it's an AI-assisted visual collaboration platform. Think digital whiteboards with AI that helps organize brainstorming sessions, create affinity diagrams, and synthesize ideas. Useful for workshops, lab retreats, and group ideation. Link at the end.

Now let's talk about two tools that address the meeting and workflow side of collaboration.

---

## SLIDE 13: Notion AI: Writing & Content
**[23:00 -- 26:00]**

Notion is a workspace tool that many of you may already use. The AI layer adds a set of features that are genuinely useful for academic work.

The writing tools work inline. You can highlight any text and ask it to simplify, expand, rewrite, adjust the tone, or translate. This is useful for things like:

- Drafting a syllabus from a bullet-point outline
- Editing an assignment prompt to be clearer
- Translating lecture notes for international collaborators
- Adjusting the tone of a workshop Q&A document

**[DEMO]**

*[Open Notion. Show highlight → simplify, expand, rewrite. Show drafting from a prompt.]*

What's important is that all of this happens inside the tool where your work already lives. You're not copying text into ChatGPT and pasting it back. It's inline, contextual, and connected to the rest of your workspace.

Notion also connects to Slack and Google Drive, so you can pull in information from tools your team already uses.

---

## SLIDE 14: Notion AI: Agents & Workflows
**[26:00 -- 29:00]**

Notion AI Agents can automate recurring tasks. Here are the use cases I think matter most for academia.

**Teaching feedback synthesis.** At the end of a semester, you have dozens or hundreds of course evaluations. An AI agent can read them all and synthesize themes: what students liked, what they struggled with, what they want changed. Instead of reading every free-text response, you get a structured summary.

**Survey processing.** For qualitative researchers, the same applies to open-ended survey responses. The agent can identify themes, categorize responses, and surface patterns.

**Meeting notes to action items.** This is the big one. Notion's AI generates meeting summaries that include tasks, owners, priority levels, and due dates. And here's the key insight: the meeting notes live *inside* Notion. So you can grab an action item from the summary, drag it into a task database, and assign it to someone on your team with a due date. No export, no copy-paste, no separate project management tool. Everything flows from the meeting into your project databases.

*[If time, show the drag-from-summary-to-task-database flow.]*

After a meeting, you update the project with new statuses, completed tasks, and revised timelines --- all in the same workspace.

---

## SLIDE 15: Notion AI: Calendar Integration
**[29:00 -- 30:30]**

As of Notion 3.1, the calendar and the AI agent are integrated.

Notion Calendar lets you add AI Meeting Notes to events, view and manage Notion databases in your calendar, and drag database items into your calendar grid. So if you create a task with a due date, it shows up on your calendar automatically.

The AI Agent can now search your Google Calendar and Notion Calendar. You can ask things like: "When did I last meet with Steven and what were the action items?" And it will find the meeting, pull up the notes, and show you what was decided.

The workflow becomes: you meet, AI captures notes, tasks are assigned with due dates, project databases are updated, and your calendar reflects the new deadlines. All automatically, all in one place.

---

## SLIDE 16: Otter AI: Where It Shines
**[30:30 -- 33:00]**

Otter AI is a transcription tool, and in some ways it overlaps with what Notion does for meeting notes. But there are five things Otter does that Notion doesn't.

**First, speaker identification.** This is the big one. When Notion transcribes a meeting, you get one long, continuous block of text --- you have no idea who said what. Otter identifies and labels individual speakers throughout the transcript. This is critical for accountability: "Maria said she'd handle the analysis by Friday." You can attribute decisions to specific people.

**Second, cross-meeting intelligence.** With Otter, you can ask questions not just about one meeting, but about a series of meetings or your entire meeting history. "What have we decided about the methodology across the last three lab meetings?" Otter can answer that. It builds a searchable knowledge base across all your meetings. Notion's notes are powerful within a single meeting but don't have this cross-meeting layer.

**Third, auto-join from calendar.** You connect Otter to your calendar and it automatically joins your meetings --- Zoom, Google Meet, Teams --- without anyone clicking anything. Notion requires someone to manually click "Start transcribing" at the beginning of every call.

**Fourth, voice-activated live participation.** This launched in March 2025. Otter's meeting assistant is no longer passive --- it's a voice-activated participant. You can literally ask Otter mid-meeting, "What did we decide about the budget last week?" and it pulls from past transcripts. In real time, during the meeting.

**And fifth, video and slide capture.** For virtual meetings where slides are being presented, Otter automatically captures screenshots of what's being shared on screen. Notion only captures audio.

There's also a pricing difference. Otter offers a free tier with 300 minutes of transcription per month. Notion's AI meeting notes require the Business plan at $20 per user per month.

The bottom line: if your meetings are simple and you already live in Notion, Notion's meeting notes are fine. If you need speaker identification, cross-meeting search, or automatic join, Otter is the better tool.

---

## SLIDE 17: Discussion
**[33:00 -- 47:00]**

Let's open it up. I want to put four questions on the table.

**First: Is struggling the point?**

We started by talking about a student who's stuck on a concept and office hours are five days away. AI solves that instantly. But here's the provocation: is working through that difficulty actually how we learn? When you struggle with a proof for three days and finally get it, you understand it at a level you wouldn't if an AI explained it in 30 seconds. Is AI-assisted learning building deeper understanding, or is it CliffsNotes-ing everything? Are we making it too easy to skip the hard parts?

*[Pause for responses. This usually generates strong opinions.]*

**Second: How does the instructor's role change?**

If AI handles tutoring, answers routine questions through the Bureaucratic Agent, generates quizzes and study materials, and even creates audio summaries --- what's left for the instructor? I'd argue what's left is the most important part: designing the learning experience, mentoring, pushing students to think critically, updating the curriculum. The repetitive work goes away, the creative and relational work stays. But not everyone sees it that way. What do you think?

*[Take 2-3 responses.]*

**Third: CliffsNotes for research?**

The literature review workflow I showed you is powerful. But there's a version of that workflow where a grad student never actually reads a paper --- they just query NotebookLM about the stack. Is that good enough? When is summary sufficient, and when do you need to sit with the original text?

*[Brief discussion.]*

**Fourth: Who benefits?**

Most of these tools are free or cheap. That's good --- it means a first-generation student with no study group can now have a personalized tutor. But it also means the students who already have advantages --- better laptops, more time, more familiarity with tech --- will adopt faster. Does this narrow the gap or widen it?

*[Open floor for remaining time.]*

---

## SLIDE 18: Resources
**[47:00 -- 48:00]**

Here are the links for everything we covered. These slides and materials will be shared after the workshop.

NotebookLM at notebooklm.google.com. Notion AI at notion.so. Otter AI at otter.ai. Curipod at curipod.com. Mizou at mizou.com. Mural at mural.co.

D-Lab at dlab.berkeley.edu for more workshops and consultations.

Thank you! I'm happy to take more questions.

---

## Q&A Buffer
**[48:00+]**

*Anticipated questions and talking points:*

- **"Can NotebookLM access my Google Drive directly?"** --- Yes, you can connect Google Drive as a source. It can also import from URLs, YouTube videos, and uploaded files.

- **"Is NotebookLM safe for sensitive research data?"** --- Google's terms say your data isn't used to train models, but it is processed on Google's servers. For IRB-sensitive data, check with your IRB first. Consider the Bureaucratic Agent use case for non-sensitive institutional documents.

- **"How does Notion AI compare to just using ChatGPT?"** --- The advantage is integration. Notion AI works inside the tool where your work already lives --- you don't copy-paste between apps. For standalone writing tasks, ChatGPT or Claude are fine. For workflow-integrated tasks, Notion is better.

- **"Is Otter worth it if I already have Zoom's built-in transcription?"** --- Zoom transcription is decent for basic transcripts, but it lacks cross-meeting intelligence, speaker identification is weaker, and there's no mid-meeting query feature. If you just need a transcript, Zoom is fine. If you need a searchable knowledge base across meetings, Otter adds real value.

- **"Can students use the Bureaucratic Agent without a Google account?"** --- NotebookLM requires a Google account. However, you as the instructor could share a read-only link to the notebook, or export the AI's responses as a FAQ document.

- **"What about privacy with Otter recording meetings?"** --- Otter notifies all participants that recording is happening. Some institutions have policies about this. Always get consent, especially for research interviews --- check with your IRB.

- **"How does NotebookLM handle conflicting information across sources?"** --- It surfaces the contradiction. If Paper A says X and Paper B says not-X, NotebookLM will note the disagreement with citations to both. It doesn't pick a side.
