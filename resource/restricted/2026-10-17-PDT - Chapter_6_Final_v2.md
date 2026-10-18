---
date: Sat Oct 17 18:20:27 PDT 2026
last_modified_at: Sat Oct 17 19:39:29 PDT 2026
layout: single
title: "[Paradigm Reset] Chapter 6: What Existing AI Discourse Gets Wrong (v2)"
permalink: /books/paradigm-reset/06/v2
categories:
 - book
tags:
 - paradigm-reset
 - AI-discourse
 - AI-governance
 - wrong-questions
 - human-machine
 - technology-determinism
 - hype-and-fear
 - regulation
 - co-design
toc: true
toc_label: "&nbsp;Table of Contents"
toc_icon: "fa-solid fa-list"
toc_sticky: true
author_profile: true
---

For about three years now I have been giving more or less the same talk in different rooms: Stanford, San Jose State, Texas A&M, Seoul National University, Korea University, KAIST, POSTECH. The slides change and the audiences change, but the first question from the back of the room never does. Someone stands up, usually a student but sometimes a professor who has waited politely through forty minutes of convex optimization and cancer biomarkers, and asks whether AI is going to replace us. When it is not that question, it is its twin: so AI is just a tool, right?

For a while I answered, and I had a good answer, with charts. Then I noticed that however I answered, the room left with exactly the picture it had come in with: humans on one side and machines on the other, a line between them, and the only question being where that line would sit next year. My answer had not touched the picture. It had only decorated it.

This chapter is about why I stopped answering that question, and three others like it.

Part I of this book was the story of a pattern that took me twenty years to see. At Samsung I found the best possible DRAM design and never once asked who had decided what "best" meant. At Amazon I helped ship an algorithm worth two hundred and seven million dollars and could not have told you whether it had made a single person's life better. At Gauss Labs I watched people on a factory floor refuse to trust an algorithm. At Erudio Bio I found that before health data can be used to save a life, someone has to answer the prior and much harder question of who owns it. Each time the technical question got answered, and each time the real question was never asked. Part II asks why, and the honest place to start is with the questions everyone else is asking, because those are the ones that crowded out the real one.

There are four of them: human versus machine, technology as destiny, hype versus fear, and regulation as follower. Each one sounds like a question. Each one is also a frame, and a frame decides in advance what will be allowed to count as an answer.

Wittgenstein wrote that the limits of my language mean the limits of my world, and although he was talking about logic, the sentence has a plainer use here. A question is a piece of language. If the only questions available about AI are these four, then there are things about AI that cannot be thought, not because they are false but because there is no sentence to think them in. Thomas Kuhn observed that most of the time scientists are not overturning anything; they are solving puzzles inside a paradigm and treating whatever does not fit as noise. The four frames are, in exactly that sense, AI's normal science. And Michel Foucault asked a question I will keep returning to, because it turns out to unlock the other four: when one way of asking becomes the obvious way, who benefits from its being obvious?

Four frames, then, taken one at a time. For each of them I will try to say what it asks, what it hides, and who gains from the hiding. By the end, I hope, the four will look less like four separate mistakes and more like one.

## The Human vs. Machine Trap

Start with the version of the question that comes with a date attached: when will artificial general intelligence arrive? The answers range from "already here" to "never," and a great deal of money and anxiety rides on the spread between them. I want to set the answers aside and look at the question itself, which is doing more work than any of the answers. "When will AI arrive at X" presupposes a finish line; a finish line presupposes a single track; and a single track presupposes that intelligence is one quantity, that it comes in amounts, and that human beings sit at some known mark on the scale, waiting to be passed.

Every part of that is doing work, and none of it survives contact with the record. In 1997 a machine beat the world chess champion, and chess stopped being the measure of intelligence roughly the following week. In 2016 the same thing happened to Go, which had been the fallback measure, and in 2020 it happened to protein folding, a problem that had defeated laboratories for fifty years and was supposed to be different. Nobody held a meeting to move the goalposts. They moved on their own, which is what goalposts do when they were never anchored to anything, and so the date keeps arriving and never arrives. When a forecast behaves that way for decades, the lesson is not that the forecasters are bad at their jobs. It is that the thing being forecast is not a thing.

The fallacy underneath is easy to see once you put two systems side by side, both built on the Transformer, the architecture behind most of what now gets called AI. One reads medical images and flags pancreatic cancer months before a radiologist would catch it. The other produces disinformation at industrial scale, thousands of plausible articles an hour, each one slightly different. Which one is more intelligent? The question has no answer, and not because we lack data about either system, but because placing both on a single axis erases the only fact about them that matters, which is what each was built to do and for whom. The intelligence spectrum is a ruler laid across things that do not share a dimension.

A footnote worth saying out loud, because almost nobody does: nobody actually uses a large language model. People use systems with a model embedded somewhere inside, wrapped in retrieval and tools and policies and an interface. The model at the core is, in plain terms, a very good estimator of which word is likely to come next. That is a description rather than an insult. It makes "how smart is it" the wrong unit of measure, in the way that "how strong is it" is the wrong unit for a bridge.

The trap's deepest room is the consciousness debate: does the machine understand, is it aware, is anything going on inside at all? Gilbert Ryle had a name for what goes wrong here, the category mistake, and his example was the visitor who is shown every college and library in Oxford and then asks, politely, where the university is. Edmund Husserl supplies the other half. Consciousness, he argued, is always consciousness *of* something and is known from within, which means that a question that can only be settled from the inside cannot ground a decision that has to be made from the outside. Whatever the truth about machine awareness turns out to be, no regulator, hospital, or court will ever have access to it. For our purposes the question is not so much wrong as idle, and I am going to leave it where it lies.

What I cannot leave alone is the trap's most popular form, because I fell into it myself and stayed there for years. Replace or assist? Will the machine take the job, or help with the job?

Let me tell you what actually happened to me. I finished my PhD at Stanford under Stephen Boyd with a command of convex optimization that fewer than a hundred people in the world share. I also left with a private embarrassment that I told almost no one about: I did not understand duality the way Boyd did. I could use it and I could teach it, but I could not see it, and that stayed true for more than a decade. Then, over a stretch of weeks, I spent hours at a time in dialogue with an AI system about duality. I asked, got an answer, pushed back because the answer was so often wrong in instructive ways, corrected it, added what I knew, and asked again. Somewhere in that back-and-forth the thing I had been missing clicked into place. The system did not understand duality, and I want to be exact about that. What it gave me was something I had never had and could not have arranged: the experience of arguing with a hundred versions of the handful of people who could have argued back, all of them patient and none of them busy. The understanding happened in me. Nothing happened in it.

Neither "replace" nor "assist" describes that. Replace is wrong on its face, since I was not replaced but changed, and assist is an understatement that misses the mechanism. The right word comes from chemistry. A catalyst lowers the barrier to a reaction and comes out the other side unchanged, with the whole transformation happening in the reactant, and so I have taken to calling what happened to me cognitive catalysis. Notice what that structure implies. In every version of this story the human supplies what the system lacks: the domain, the question, the stubbornness, the desire to understand. A stronger catalyst does not make those contributions less valuable. It makes them decisive.

The jobs question is the same trap with a salary attached. Which jobs are safe, and which will disappear? Ask it and you can only get back lists, winners and losers sorted by occupation, and the lists will be wrong in the way AGI dates are wrong and for the same reason: they assume the technology arrives with its uses already decided. The better question is not which existing jobs survive the machine but what new forms of work and collaboration we want to create with it. Jobs are not found inside a technology like fossils in rock; somebody designs them, and the design is a choice that could have gone otherwise. Chapter 8 will argue that the line between human work and machine work has always been drawn by agreement rather than discovered, and that it is being drawn again now, mostly by people who would prefer you did not notice.

That is the skill this section is for. When you hear a question framed as humans against machines, whether it arrives as an arrival date, a ranking, a consciousness debate, or a layoff forecast, stop and name the hidden premise, which is always some version of one axis, one finish line, one contest. Then put the question back in a form we can act on. Not "when will it match us?" but "what are we building together, and who decides?"

Drop the contest, though, and something else rushes in to fill the space. If it is not us against them, then surely the technology simply advances on its own and we adjust as best we can. That reflex is the second frame.

## The Technology Determinism Myth

The word "innovation" does moral work it has never been asked to justify. It names a change and grades the change in the same breath, and you can feel the grade built into the word by noticing that nobody says "a harmful innovation" without the sentence sounding slightly off. From there it is a short step to the assumption that sits under most writing about AI, usually without being stated: innovation is progress, progress is inevitable, and the only open question is how quickly we adapt.

I believed a version of this for most of my career, and I had the best possible excuse. The Prologue opened in a Vancouver office in August 2019, with a screen showing the result of an A/B test: two hundred and seven million dollars in revenue attributable to a personalization algorithm my team had built. By any definition of innovation I knew at the time, it qualified. I remember the feeling precisely, and it was not triumph. It was the feeling of having answered, brilliantly, a question nobody had asked. Progress for whom? The objective function had never been given that question, so it had no opinion, and neither, I realized standing there, did I.

What the determinist frame hides is this. Every system I have ever built embedded three choices that nobody in the room called choices: what to optimize, what data to trust, and what error to tolerate. Chapter 7 takes up the first two and Chapter 11 the third, so I will only point at them here. But I want to insist that they were choices, because the frame's whole trick is to make them look like facts about the technology.

Take the proudest moment of my thirteen years at Samsung. In 2009 my group redesigned a DRAM cell with the optimization platform I had built, and the head of the DRAM team said something I still quote. It was the first time in his career, he said, that he could say with certainty a design was the best possible one. He was right, and I am still proud of it. But "best" meant best under the objective I had been handed, performance and power and area in weights that someone had set, and the physics did not choose those weights. A meeting chose them, somewhere above my pay grade and well before I arrived, and by the time the problem reached me the weights had hardened into requirements that nobody thought of as anyone's decision. That, most of the time, is what technological determinism is: not a property of the technology at all, but what a choice looks like after the people who made it have left the room.

If the technology really did determine the outcome, the same technology would produce the same outcome everywhere, and it does not. Nuclear fission works identically in every country. Yet France built most of its electricity around it, Germany shut down its last reactor in 2023 after decades of argument and a vote, and several countries with every bit of the necessary engineering capacity never built a plant. The physics was constant and the societies were not. Whatever determined those outcomes, it was not the reactor.

Social media is the nearer parallel, because the choice is still visible if you know where to look. A feed sorted by what keeps people scrolling was not discovered inside the technology. It was chosen, in rooms I can picture because I have sat in their equivalents, and the choice was defensible on every metric those rooms were tracking, since engagement went up and revenue went up and the dashboards were green. The harms that followed, the polarization and the compulsive use and a public that could no longer agree on what had happened, arrived through exactly the mechanism that made the metrics go up. Nothing in the technology required that objective. Chapter 15 argues that we are now repeating the pattern with AI, step for step.

Jean-Paul Sartre has a sentence that belongs here. Existence precedes essence: we are not born with a nature and then live it out, but act first and become something through the acting. The same is true of a technology, which has no essence waiting to unfold prior to the decisions people make about what to build, on what data, and to what end. Sartre also had a name for the move of handing your freedom to an object so that you will not have to be responsible for what you do with it, and he called it bad faith. Technological determinism is bad faith at the scale of an industry.

Which is why the myth persists: it relieves everyone. Engineers did not choose, they implemented; executives did not choose, they responded to the market; regulators could not have chosen, because the technology moved too fast. A frame in which nobody is responsible will never lack for sponsors. Foucault's question returns in a sharper form: when a way of talking makes no one accountable, look for who is spared.

The skill, then, is to take any claim about what AI will do and split it in two, into the part that is trajectory, the new capability, and the part that is choice, what someone decided to do with it. Then go looking for the three choice points. Who set the objective? Who picked the data? Who decided how much error was acceptable, and acceptable to whom? If you cannot find them, you are not looking at a fact about the technology. You are looking at a choice that someone has hidden, possibly even from themselves.

Determinism has two moods. In a good mood it promises abundance, cures, the end of drudgery; in a bad mood it predicts extinction; and both moods agree on the one thing that matters, which is that the outcome is coming regardless of what we do. They are one frame wearing two faces, and those two faces are the third frame.

## The Hype/Fear Binary

Go to any AI conference this year and wait, because it does not take long. Somewhere in the first panel a moderator will lean toward the microphone and ask the question the room has been waiting for: is AI safe, or is it dangerous? The audience sorts itself within minutes. You can watch it happen in the nods and the folded arms. And because I build these systems for a living, sooner or later someone turns to me and asks which side I am on.

The two sides are familiar enough to sketch in a sentence each. On one, AI cures the diseases we could not cure, ends the drudgery we could not escape, and delivers an abundance that makes the old scarcities look quaint. On the other, it empties the labor market, floods the public square with manufactured lies, and, in the strong version, ends us. Utopia and dystopia. Both are wrong in the same way, and the way they are wrong is a good deal more instructive than either of them.

The error is one we have met already, in a different costume. AI is a capability, not an agent with intentions. A knife in a chef's hand feeds a family, and the same knife in another hand takes a life. We do not convene panels on whether knives are safe; we ask who is holding one, in what setting, and under what rules. Recall the two systems from earlier in this chapter, built on the same architecture, one flagging pancreatic cancer and the other manufacturing disinformation. If "safe" or "dangerous" were a property of the architecture, those two systems could not both exist. Since they plainly do, the property must live somewhere else, in the people and institutions that chose what to build and where to point it.

Which means that "AI is dangerous" and "AI is safe" are the same sleight of hand performed in opposite directions. Both locate the moral weight in the machine, and both let the humans leave the stage.

Why is that evasion so tempting? I can think of three reasons, and each one has a beneficiary.

The first is psychological. If the danger is in the machine, then the problem is technical, and technical problems are the kind we know how to make progress on, by benchmarking them, funding them, and building teams around them. The alternative is to admit that the problem is us, and human wisdom, unlike compute, does not double every eighteen months. A technical problem is simply a more comfortable thing to have than a civilizational one.

The second is political, and here the two frames split the spoils between them. Fear hands governments regulatory authority they would otherwise have to argue for, and it hands researchers a funding line. It also hands incumbents a barrier to entry, since compliance is cheap at scale and ruinous for a startup, and a large company that calls for strict regulation is rarely acting against its own interests. Hype does the mirror work. It raises capital, it justifies concentration as the price of progress, and it defers every hard question to a future that the hyped party expects to control. Fear and hope disagree about everything except the one thing that matters, which is who ends up holding the pen.

The third is philosophical. We have not done the contemplative work. We are applying moral categories built in the nineteenth century, for locomotives and bridges and medicines whose risks were bounded and local, to a technology whose reach is not bounded in that way. The categories do not fit. Rather than build new ones, we have spent a decade arguing about which of the old ones to apply.

This is where Foucault stops being a footnote and becomes a tool. A discourse, he argued, does not merely describe its objects; it produces them. "AI safety," spoken often enough and by the right people, produces a world in which a small number of laboratories are the natural guardians of a danger that only they are equipped to measure. "AI abundance," spoken just as often, produces a world in which the same laboratories are the natural stewards of the coming plenty. The content of the two stories could not be more different. The cast is identical.

So what is in the middle? Not moderation, and not "somewhat safe" or "dangerous but manageable," which are just the binary with the volume turned down. The middle is a different axis, and getting onto it takes a kind of lucidity that Camus would have recognized: neither hope nor despair, but a refusal to look away from the thing as it actually is.

And the thing as it actually is turns out to be sociotechnical. No AI system is deployed into a vacuum. It arrives inside an organization with incentives, a market with competitors, a legal regime with gaps, and a population with habits, and it behaves as all of those behave. Trying to make a system of many interacting agents safe by aligning each agent on its own is like trying to make a city safe by handing every citizen a handbook. Diagnosing the danger of an AI deployment by examining the algorithm is like diagnosing a patient by examining the left elbow. The elbow is real. It is just not where the illness is.

Once you are on that axis, the question "safe or dangerous" dissolves into four harder ones. What institutions do we need for a general-purpose technology, institutions with real enforcement capacity rather than white papers? Who gets to concentrate it, in a world where a single firm can deploy a thousand instances of an AI legal system in the time it would take to interview one lawyer? What are humans for, once most cognitive labor becomes cheap? And are we, as a civilization, mature enough to be trusted with this? Chapters 7 and 10 take up the first two, Chapter 13 takes up what autonomy means under these systems, and the last two run underneath the whole series. None of them has a checkbox answer, which is exactly why the binary is so attractive and so useless.

Two philosophers give the middle its working tools. John Rawls asked what arrangements you would accept if you did not know which position in society you would occupy. The AI version of his question is whether you would accept this design not knowing whether you will be the patient or the radiologist, the rider or the driver, the person flagged or the person reviewing the flag. Michael Sandel asked which things should not be for sale, however efficient the market. The AI version of his is which decisions should not be delegated, however accurate the model, and Chapter 8 takes up which ones.

What to do, then, when someone offers you "safe or dangerous": decline the side. Name whom each side serves, which is usually the same people, and then move to the axis where the real questions live: what institutions, whose concentration, what human purpose, and how much wisdom.

And if the answer to "safe or dangerous" is design and governance, the reflex that follows is as predictable as the panel question was. Who governs? Regulators, of course, later, once they have caught up. That reflex is the fourth frame.

## The Regulation-Follows-Technology Frame

The fourth frame comes with its own picture, and the picture is a race. Technology runs ahead on its own legs; policy chases it, out of breath and always a few years behind, and the best anyone hopes for is that the gap does not grow. "Regulators must catch up" is how the picture gets said aloud. Notice that it is simply the second frame in a different setting, because if technology moves by itself, then of course the law can only follow it. Accept determinism and the race is already lost.

I want to say plainly that the picture does not match anything I have built. No system I have ever shipped arrived in a legal vacuum and waited for the law to notice it. At Erudio Bio the regulatory pathway was in the room from the first design meeting. What data we could touch was governed by institutional review before we touched it, and what the system would be allowed to claim was shaped by how MFDS, Korea's food and drug regulator, and the FDA in the United States evaluate a diagnostic. That shaped what we chose to build, not what we did afterward. At Amazon, personalization did not run wherever the algorithm pointed; internal review processes decided what it was allowed to touch. At Samsung, before I optimized a single DRAM cell, industry standards had already decided what a DRAM cell could be.

The law is not behind the technology. It is inside it. Intellectual property decides what can be copied, liability decides who pays when something fails, corporate form decides who is accountable and to whom, procurement rules decide which systems governments will buy, and data access rules decide what can be learned from. Every one of these was in force before the first line of code was written, and every one of them shaped the code. "Catch up" pretends the law is absent when it is only invisible, and an invisible rule is a rule that nobody is arguing about.

That is who the frame serves. In a race where regulators are permanently behind, the leader writes the rules by default, in the shape of defaults, terms of service, and facts on the ground that are expensive to reverse. "Give us time to innovate before you regulate" sounds like a plea for freedom, and is in practice a request to hold the pen while everyone else is still finding their seats. Chapter 14 takes this frame apart in full; here I only want to replace the picture.

The replacement is co-design, and I can state it in three sentences because Chapter 14 and Book III do the real work. Error tolerance, acceptable risk, and the allocation of responsibility are decided during development whether or not anyone admits it, and earlier in this chapter we found all three hidden inside every system I have built. Co-design means deciding them on purpose, with people other than the builders in the room when the deciding happens. It does not slow the technology down; it changes who gets to say what the technology is for.

If that sounds like a brake, the historical record says otherwise. Commercial aviation did not grow despite safety certification; certification is what made strangers willing to board an aircraft flown by someone they had never met, and the passenger market was built on that willingness. Drug approval is the same story. A patient cannot evaluate a molecule, and review by a body the patient has reason to trust is what makes a market for medicine possible at all. Erudio Bio's path through MFDS and the FDA is not an obstacle to having customers; it is the condition of having them. The internet grew on shared protocols set by open bodies before anyone had scaled anything. Rules first, scale second, in each case.

Thomas Aquinas defined law as an ordinance of reason for the common good, made by those who have care of the community. That is not a brake bolted on after the machine is running; it is a statement, made in advance, of what the community is for. Augustine, eight centuries earlier, had said that a people is defined by the common objects of its love. Put the two together and you have the alternative to the race. What we build reveals what we love, and law is where we say so out loud, before we build it.

The fourth skill follows directly. When you hear "regulators must catch up," find the law that is already inside the system, the property rules, the liability rules, the standards, the procurement, the data access, and then ask who benefits from pretending it is not there. Usually it is whoever is currently ahead.

## Four Frames, One Structure

I promised at the start that by the end the four frames would look less like four mistakes and more like one, so here they are side by side.

**Table 6.1. The four frames of existing AI discourse**

| The frame | What it asks | What it hides | Who benefits from the hiding |
|---|---|---|---|
| Human vs. machine | When will AI match us? | What collaboration are we designing, and who decides? | Whoever profits from a contest, and from selling the finish line |
| Technology as destiny | What will AI do to us? | What are we choosing, and who chose? | Everyone who would rather not be responsible |
| Hype vs. fear | Is AI safe or dangerous? | Safe for whom, decided by whom? | Incumbents, regulators, and funders on both sides |
| Regulation as follower | How do regulators catch up? | Who is already writing the rules by default? | Whoever is currently ahead |

Read down the third column and the structure appears. Each frame takes the decisive choice and moves it somewhere no one can be held to account for it, into the machine, into history, into the future, into a race that nobody can win. Four frames making the same move is not four accidents. It is what a discourse looks like when it has been shaped, over years and without anyone needing to conspire, by the people it spares.

Thomas Kuhn, whom I mentioned at the start, was clear that paradigms do not fall to arguments. They fall when anomalies pile up past the point where the old frame can absorb them, and someone offers a new frame in which the anomalies turn out to be the normal case. This chapter was the pile. The chapters that follow are the offer, beginning in Chapter 7 with the claim that AI is not a technology to be controlled but a device that redistributes power and redesigns the choices available to everyone it touches.

> **Governance Insight** — *Jeff Lee and Hayden Song*
>
> The questions we ask determine the solutions we see. If we ask "When will AI be as smart as humans?" we design Turing tests. If we ask "How should AI reshape power?" we design governance structures. Current AI discourse asks the wrong questions because existing power structures benefit from those questions.

Back to the lecture hall, then. These days, when someone at the back stands up and asks whether AI will replace us, I answer with a question of my own: replace us at what, and chosen by whom? The room usually goes quiet for a moment, and that silence is where the rest of this book lives.
