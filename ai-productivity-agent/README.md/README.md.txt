# AI Personal Productivity Assistant — RAG

A Retrieval-Augmented Generation (RAG) based personal productivity assistant.

The system retrieves relevant information from a productivity knowledge base and uses a local language model to generate a grounded response.

## RAG Pipeline

PDF Knowledge Base
        ↓
Text Extraction
        ↓
Text Chunking
        ↓
Sentence Embeddings
        ↓
ChromaDB Vector Store
        ↓
Similarity Search
        ↓
Retrieved Context
        ↓
Local Qwen LLM
        ↓
Generated Response

## Technologies Used

- Python
- PyPDF
- Sentence Transformers
- ChromaDB
- Hugging Face Transformers
- PyTorch

## Models

### Embedding Model

`all-MiniLM-L6-v2`

Used to convert document chunks and user queries into vector embeddings.

### Language Model

`Qwen/Qwen2.5-0.5B-Instruct`

The language model runs locally using Hugging Face Transformers.

## Knowledge Base

PDF documents are placed inside:

`data/raw/`

The system extracts text from the PDFs, splits the text into overlapping chunks, generates embeddings, and stores them in ChromaDB.

## Retrieval

For each user query:

1. The query is converted into an embedding.
2. ChromaDB performs similarity search.
3. The top relevant chunks are retrieved.
4. The retrieved chunks are added to the prompt.
5. The local Qwen model generates the final response.

## Grounded Generation

The model is instructed to answer using only the retrieved productivity context and not invent policies.

## Current Implementation

The current implementation uses an in-memory ChromaDB collection. The vector database is rebuilt when the program runs.

## Project Structure

```text
ai-productivity-agent/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── raw/
│       └── knowledge_base.pdf
│
├── src/
│   ├── ingestion.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retrieval.py
│   ├── generation.py
│   └── main.py
│
└── experiments/
    └── README.md

---

## What about your PDF?

Put your actual PDF here:

Personal Productivity Knowledge Base
Synthetic reference data for a RAG-powered personal productivity agent. This document contains the type of
information an agent should retrieve when planning a user's day. It intentionally uses a realistic fictional profile so it
can be used safely for development and testing.
1. User Profile and Working Style
Profile: The user is a college student preparing for product-based company placements while building technical
projects and improving software-engineering skills.
Primary ambition: Become highly capable in product engineering and eventually build meaningful technology
products.
Working philosophy: The user values ambitious goals, continuous improvement, independence of thought, high
standards, and disciplined execution.
Learning style: Prefers practical learning through building projects, solving coding problems, reading, and
understanding concepts rather than memorizing them.
Planning preference: Prefers a realistic schedule with enough buffer between tasks. Overly packed schedules
reduce follow-through.
Focus preference: Difficult technical work is best scheduled during longer uninterrupted blocks. Administrative or
lightweight work can be placed in shorter gaps.
Task preference: Important tasks should be explicitly prioritized instead of treating every task as equally urgent.
2. Long-Term Goals
Goal
Description
Priority
Product engineering career
Prepare for product-based technology companies and become strong in software engineering fundamentals.
High
DSA proficiency
Project portfolio
AI engineering
Communication
Reading
Build strong data structures and algorithms problem-solving ability for technical interviews.
High
Build technically substantial projects that demonstrate engineering ability.
High
Learn RAG, LLM applications, agents, APIs, vector databases, and AI system design.
High
Improve professional communication, explanations, presentations, and documentation.
Medium
Maintain a consistent reading habit covering finance, psychology, business, and personal development.
Medium
3. Current Focus Areas
• Placement preparation, especially DSA and product-engineering fundamentals.
• Building an AI productivity-agent project using RAG, vector search, LLM reasoning, and tool calling.
• Improving Java and general programming problem-solving ability.
• Developing a strong project portfolio instead of relying only on certificates.
• Learning how production software systems are designed and deployed.
• Maintaining a sustainable reading habit.
4. Current Projects
Project A — RAG Productivity Agent: A desktop AI agent that launches when the laptop starts, retrieves relevant
personal context, checks tasks and schedules, and generates or updates a daily plan. It uses RAG for semantic
memory and structured storage for authoritative task state.
Project B — Metro Passenger Self-Service Locker Concept: A concept for self-service luggage lockers targeted
specifically at metro passengers. The system is intended to be accessible to passengers directly rather than being a
general-purpose locker service for outside travelers.
Project C — Placement Preparation System: A structured effort to improve DSA, programming,
product-engineering knowledge, project quality, and interview readiness.
5. Productivity Rules
• Deadlines closer than one or two days should receive strong priority.
• Overdue tasks should be surfaced instead of silently forgotten.
• An unfinished high-priority task from yesterday should usually be considered before adding low-value new tasks.
• Do not schedule every available minute. Leave realistic buffers.
• Long technical tasks should preferably be placed in uninterrupted focus blocks.
• Avoid scheduling multiple cognitively heavy tasks back-to-back when a break is practical.
• If a task has no deadline and low importance, it can be moved to a later day.
• The schedule should reflect the user's actual available time, not an idealized 16-hour workday.
• When there is insufficient time to complete everything, prioritize rather than compressing every task unrealistically.
• The agent should explain major prioritization decisions when useful.
6. Scheduling Preferences
Preferred daily structure: A few meaningful high-priority tasks plus smaller secondary tasks.
Focus sessions: Technical work is preferably scheduled in approximately 60–120 minute blocks.
Breaks: Short breaks should be available between demanding work blocks.
Buffer: At least some unscheduled time should remain available for unexpected college work, delays, or task
overruns.
Morning: Prefer difficult/high-value work when possible.
Evening: Suitable for reading, review, lighter coding, planning, and unfinished tasks.
Overloaded day: If the requested workload exceeds available time, identify what should be postponed rather than
pretending everything fits.
7. Placement Preparation Knowledge
The user is targeting strong product-based technology companies through college placements. Preparation should
therefore balance several areas.
• Data structures and algorithms: arrays, strings, hashing, linked lists, stacks, queues, trees, graphs, recursion,
dynamic programming, sorting, searching, and complexity analysis.
• Programming: strong Java fundamentals, object-oriented programming, debugging, clean code, and implementation
speed.
• Computer science fundamentals: operating systems, DBMS, computer networks, object-oriented design, and basic
system design.
• Projects: ability to explain architecture, technical decisions, trade-offs, challenges, and measurable outcomes.
• Aptitude and communication: useful where required by placement processes.
• Interview readiness: coding under time pressure, explaining reasoning clearly, and discussing projects deeply.
8. AI Engineering Learning Priorities
• RAG fundamentals: ingestion, chunking, embeddings, vector search, retrieval, reranking, context construction, and
evaluation.
• Vector databases: understand how semantic search works and when metadata filtering is useful.
• LLM application design: prompting, structured outputs, function/tool calling, context management, and evaluation.
• AI agents: tool use, planning, state, memory, controlled actions, and error handling.
• Backend engineering: APIs, authentication, persistence, logging, and deployment basics.
• System design: separating deterministic application state from probabilistic LLM reasoning.
9. Reading and Knowledge Development
The user values reading as part of personal development. Reading should not replace core placement preparation
but can be scheduled as a lower-intensity activity when appropriate.
Example reading interests: personal finance, psychology, business, decision-making, discipline, human behavior,
and personal development.
Example current reading reference: The Psychology of Money. Useful concepts include behavior around money,
long-term thinking, risk, compounding, and the difference between wealth and visible spending.
Scheduling rule: Reading can be placed in a 20–45 minute evening block when high-priority technical tasks are
already handled.
10. Example Tasks and Priorities
Task
Duration
Priority
Solve 5 DSA problems
Build RAG retrieval pipeline
90 min
120 min
High
High
Typical reasoning
Placement preparation
Current AI project
Fix Java assignment
Read 20 pages
120 min
30 min
Update LinkedIn/project documentation30 min
Watch random technical videos
60 min
High
Medium
Low/Medium
Low
11. Historical Daily Plan — September 5
Academic deadline
Personal development
Portfolio maintenance
Useful only after priority work
Planned: DSA practice, AI project research, college documentation, reading.
Completed: DSA practice and college documentation.
Unfinished: AI project research and reading.
Reflection: The AI research task took longer because the user spent additional time understanding vector databases
and RAG architecture.
Planning implication: Future AI project sessions should use longer uninterrupted blocks and should not be
underestimated.
12. Historical Daily Plan — September 6
Planned: Java coding practice, AI project architecture, placement research.
Completed: Java coding practice.
Unfinished: AI architecture work.
Reflection: Switching repeatedly between placement research and coding reduced focus.
Planning implication: Group similar technical activities together rather than repeatedly switching contexts.
13. Historical Daily Plan — September 7
Planned: DSA, project work, college activity, professional profile update.
Completed: DSA and college activity.
Unfinished: Project work and professional profile update.
Reflection: College responsibilities consumed more time than expected.
Planning implication: Keep buffer time on college-heavy days.
14. Historical Daily Plan — September 8
Planned: Finish Java assignment, work on AI productivity agent, DSA practice.
Completed: DSA practice.
Unfinished: Java assignment and AI productivity-agent work.
Reflection: The user underestimated the time required for the project architecture.
Planning implication: On the next day, prioritize the Java assignment if its deadline is approaching, then allocate a
dedicated project block.
15. Example Upcoming Deadlines
Date
Item
Priority
September 10
Java assignment
High
Planning note
Should be completed before low-priority work.
September 12
September 15
September 20
College documentation
AI project review
Placement preparation milestone
Medium
High
High
Can be scheduled in a shorter administrative block.
Reserve multiple project sessions before the review.
Maintain recurring DSA and CS fundamentals practice.
16. Calendar Constraints — Example
The following are fictional calendar commitments used for testing scheduling logic.
Time
Event
Type
09:30–10:30
College lecture
Fixed
11:30–12:00
13:00–14:00
16:00–17:00
Placement preparation group discussion
Lunch / personal time
College project meeting
17. Example Daily Planning Scenarios
Fixed
Blocked
Fixed
Scenario A — Existing tasks: If today's database contains a high-priority assignment due tomorrow, an AI project
session, and DSA practice, the agent should consider the deadline and recent unfinished work before lower-priority
activities.
Scenario B — No scheduled tasks: If no tasks exist, the agent should ask the user what needs to be accomplished
instead of inventing a plan.
Scenario C — Too many tasks: If the user gives eight hours of work but only five hours are realistically available,
the agent should identify the highest-value tasks and propose moving the rest.
Scenario D — Task overrun: If a two-hour project task takes three hours, the agent should recalculate the
remaining schedule rather than simply adding another three-hour block.
Scenario E — New urgent task: If the user says an assignment is due tomorrow, the agent should update priority
and reconsider today's schedule.
18. Natural-Language User Inputs
• "I need to finish my Java assignment, do DSA for two hours, and work on the AI project."
• "I couldn't finish the project yesterday. Move it to today."
• "I have a placement discussion at 11:30."
• "I have three hours free this afternoon. What should I work on?"
• "The assignment is due tomorrow, so make sure it gets done today."
• "I am tired today. Give me a lighter schedule."
• "I finished the Java assignment. What should I do next?"
19. Retrieval Examples for Testing RAG
Query: What unfinished work should I consider today?
Relevant knowledge: Recent daily plans and unfinished tasks.
Query: What are my highest-priority goals?
Relevant knowledge: Long-term goals and current focus areas.
Query: Why should I leave buffer time?
Relevant knowledge: Scheduling preferences and historical reflections.
Query: What project am I currently building?
Relevant knowledge: Current projects and AI engineering learning priorities.
Query: What deadline is closest?
Relevant knowledge: Upcoming deadlines; authoritative date should ultimately come from structured task/calendar
data.
Query: What happened when I scheduled too much technical work?
Relevant knowledge: Historical plans and reflections.
20. Facts vs. Suggestions
Known facts in this knowledge base: Goals, project descriptions, historical plans, example deadlines, preferences,
and calendar constraints explicitly documented here.
Agent suggestions: Proposed schedules, estimated priorities, and rescheduling decisions are generated
dynamically and should not be stored as permanent facts unless the user accepts them.
Important rule: Retrieved historical information can inform a plan, but the agent should not assume that an old task
is still active without checking current structured task state.
21. RAG Metadata Recommendations
Each indexed chunk should ideally contain metadata such as: source_type, date, project, topic, task_id, status,
priority, and content_type.
Examples of content_type values: goal, preference, daily_plan, reflection, project_context, deadline_context,
calendar_context, learning_note.
22. Example Memory Records
Memory: "AI project architecture took longer than expected on September 8."
Memory: "Context switching between coding and research reduced focus on September 6."
Memory: "College responsibilities can consume more time than planned; leave buffer."
Memory: "High-priority technical work is better handled in long uninterrupted sessions."
23. Agent Decision Principles
• Retrieve relevant memory before making a personalized recommendation.
• Use current structured task/calendar state as the source of truth.
• Use historical memory to understand patterns and context, not to override current facts.
• Prioritize based on urgency, importance, deadlines, and strategic goals.
• Avoid overloading the schedule.
• Ask for clarification when critical information is missing.
• Clearly distinguish confirmed tasks from recommendations.
• When the user changes a plan, update structured state and optionally store the new decision as memory.
24. Test Dataset Summary
This knowledge base intentionally contains multiple information types that require different retrieval behavior: stable
user goals, semi-stable preferences, current projects, historical daily plans, reflections, deadlines, calendar
constraints, and example tasks. It is designed to test whether a RAG system can retrieve the right context instead of
simply returning the most recently stored document.

data
└── raw
    └── knowledge_base.pdf