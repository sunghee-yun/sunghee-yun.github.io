---
date: Sat Oct 17 22:10:26 PDT 2026
last_modified_at: Sat Oct 17 22:12:09 PDT 2026
layout: single
title: "[Paradigm Reset] Chapter 6: What Existing AI Discourse Gets Wrong"
permalink: /books/paradigm-reset/06/v5
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
toc: true
toc_label: "&nbsp;Table of Contents"
toc_icon: "fa-solid fa-list"
toc_sticky: true
author_profile: true
---

For about three years now I have been giving more or less the same talk in different rooms: Stanford, San Jose State, Texas A&M, Seoul National University, Korea University, KAIST, POSTECH. The slides change and the audiences change, but the first question from the back of the room never does. Someone stands up, usually a student but sometimes a professor who has waited politely through forty minutes of convex optimization and cancer biomarkers, and asks whether AI is going to replace us. When it is not that question, it is its twin: so AI is just a tool, right?

For a while I answered, and I had a good answer, with charts. Then I noticed that however I answered, the room left with exactly the picture it had come in with: humans on one side and machines on the other, a line between them. The only question worth asking was where that line would sit next year. My answer had not touched the picture. It had only decorated it.

The question changes its clothes with the audience but not its shape. In rooms full of policymakers, nobody asks whether AI will replace anyone; they ask how far behind the country is and how fast it must run to catch up. The numbers I give in answer settle into the same picture: a race with a track, a finish line somewhere ahead, and the only question being our position on the track. Nobody asks who laid out the track, or what is waiting at the end of it.

This chapter is about why I stopped answering those questions, and two others like them.

Part I of this book was the story of a pattern. At Samsung I found the best possible DRAM design and never once asked who had decided what "best" meant. At Amazon I helped ship an algorithm worth two hundred and seven million dollars and could not have told you whether it had made a single person's life better. At Gauss Labs I watched people on a factory floor refuse to trust an algorithm, and at Erudio Bio I found that before health data can save a life, someone has to answer the harder question of who owns it. Each time the technical question got answered, and each time the real question was never asked. Part II asks why, and the honest place to start is with the questions everyone else is asking, because those are the ones that crowded out the real one.

There are three of them: human versus machine, technology as destiny, and hype versus fear. Each one sounds like a question. Each one is also a frame, and a frame decides in advance what will be allowed to count as an answer.

I learned what that means from optimization before I learned it from anything else. When you set up a problem, the first thing you write down is not the objective. It is the set of things the solver is allowed to consider, and everything outside that set is invisible to it, no matter how clever the algorithm. If the best design in the world lies outside the set you wrote down, the solver will never find it, and will report its best answer with complete confidence. A question works the same way on a mind. Ask "when will AI replace us" and you have written down a set in which every answer is a date and a direction. The things that lie outside that set are not wrong. They are simply unreachable from where you started.

That is why this chapter is about questions rather than answers, and why I will keep returning to one question in particular: when a way of asking becomes the obvious way, who benefits from its being obvious? The three frames did not become dominant by being true. They became dominant by being useful to someone, and the someone is usually not the person asking.

Three frames, then, taken one at a time. For each I will say what it asks, what it hides, and who gains from the hiding, and at the end there is a table that puts them side by side. By then I hope they will look less like three separate mistakes and more like one. This chapter dismantles; the building begins in Chapter 7.

## The Human vs. Machine Trap

### The date that never arrives

Start with the version of the question that comes with a date attached: when will artificial general intelligence arrive? The answers range from "already here" to "never," and a great deal of money and anxiety rides on the spread between them. I want to set the answers aside and look at the question itself, which is doing more work than any of the answers.

The forecasting record is worth a moment, because it is long and it is consistent. In 1950 Alan Turing predicted that by the end of the century a machine would hold a five-minute conversation well enough to fool an ordinary questioner about a third of the time. In 1957 Herbert Simon predicted that within ten years a computer would be the world chess champion. In 1970 Marvin Minsky told Life magazine that in three to eight years we would have a machine with the general intelligence of an average human being. These were among the most capable people of their century, and each was wrong in the same direction, with the same confidence, about the same thing.

Then look at what happened when the machines did arrive. In 1997 a machine beat the world chess champion, and chess stopped being the measure of intelligence roughly the following week. In 2016 the same thing happened to Go. In 2020 it happened to protein folding, a problem that had defeated laboratories for fifty years. Nobody held a meeting to move the goalposts. They moved on their own, which is what goalposts do when they were never anchored to anything, and so the date keeps arriving and never arrives. A question answered wrongly for seventy years is still the first one asked, and the reason is not that the answer is useful. It is that the question is useful. It raises money, it frightens, and above all it defers: as long as the date is somewhere ahead, every harder question can wait.

When a forecast fails for seventy years in the same way, the lesson is not that the forecasters are bad at their jobs. It is that the thing being forecast is not a thing. "When will AI arrive at human level" presupposes a finish line, and a finish line presupposes a single track. A single track presupposes that intelligence is one quantity, that it comes in amounts, and that human beings sit at some known mark on the scale, waiting to be passed. Every link in that chain is doing work, and none of them survives contact with the record.

### The intelligence spectrum fallacy

The fallacy underneath is easy to see once you put two systems side by side, both built on the Transformer, the architecture behind most of what now gets called AI. One reads medical images and flags pancreatic cancer months before a radiologist would catch it. The other produces disinformation at industrial scale, thousands of plausible articles an hour, each slightly different so that no filter catches them all. Which one is more intelligent? The question has no answer, and not because we lack data about either system. It has no answer because placing both on a single axis erases the only fact about them that matters, which is what each was built to do and for whom. The intelligence spectrum is a ruler laid across things that do not share a dimension.

The robotics community noticed a version of this forty years ago and gave it a name. Moravec's paradox is the observation that the things humans find hardest, such as symbolic reasoning, chess, and calculus, turned out to be easy for machines. The things any four-year-old does without effort, such as recognizing a face, walking across a cluttered room, or knowing that a cup will spill, turned out to be fiendishly hard. If intelligence were one quantity, that could not happen; a machine that was "smarter" than a child would be smarter at everything. The paradox dissolves as soon as you drop the single axis, which is to say it was never a paradox about machines. It was a paradox about the ruler.

A footnote worth saying out loud, because almost nobody does: nobody actually uses a large language model. People use systems with a model embedded inside, wrapped in retrieval and tools and policies and an interface that someone designed, and the model at the core is, in plain terms, a very good estimator of which word is likely to come next. That is a description, not an insult. It makes "how smart is it" the wrong unit of measure, in the way that "how strong is it" is the wrong unit for a bridge. A bridge is strong in some directions and not others, by design, for a particular river.

### The consciousness question

The trap's deepest room is the consciousness debate. Does the machine understand what it says? Is it aware? Could it suffer? These are real questions with a long literature, and I am going to set them aside in a few paragraphs, for a reason I want to explain.

Whatever understanding or awareness is, it is known from the inside, by whoever has it. For a machine built nothing like us, the inference we make about other people has no footing, so the question can only be settled from a position nobody outside the machine can occupy. But every decision we have to make about these systems is made from outside, and no regulator, hospital, or court will ever have access to the inside answer.

Try the thought experiment the other way. Suppose it were settled tomorrow, beyond dispute, that some machine was conscious. We would still need to decide who may deploy it, for what, with what error rate, and who answers when it fails. We would have acquired a new obligation toward the machine, which is no small thing, but we would not have discharged a single one of our obligations toward each other. A question whose answer changes nothing you are about to do is a question you can set down. So for the purposes of this book the consciousness question is not wrong so much as idle, and I am going to leave it where it lies, with respect, and get on with the questions that move something.

### Replace or assist: what actually happened to me

What I cannot leave alone is the trap's most popular form, because I fell into it myself and stayed there for years. Replace or assist? Will the machine take the job, or help with the job? Every panel I have sat on has eventually arrived at it.

Let me tell you what actually happened to me. I finished my PhD at Stanford under Stephen Boyd with a command of convex optimization that fewer than a hundred people in the world share. I also left with a private embarrassment that I told almost no one about: I did not understand duality the way Boyd did. I could use it and I could teach it, but I could not see it, and that stayed true through Samsung and Amazon and a startup, for more than a decade. Then, over a stretch of weeks, I spent hours at a time in dialogue with an AI system about duality. I asked, got an answer, pushed back because the answer was so often wrong in instructive ways, corrected it, added what I knew, and asked again. Somewhere in that back-and-forth the thing I had been missing for twelve years clicked into place, and it has stayed in place.

The system did not understand duality, and I want to be exact about that. It was closer to a sparring partner who never tires and never takes offense, and whose mistakes were as useful as its answers. What it gave me was something I had never had and could not have arranged: the experience of arguing with a hundred versions of the handful of people who could have argued back, all of them patient and none of them busy. The understanding happened in me. Nothing happened in it.

Once I had seen the shape of that, I started seeing it everywhere, and it is easiest to show with two scenarios of the kind I now use in lectures. Picture a physician who asks the system for fifteen differential diagnoses. She dismisses twelve of them in under a minute, because she has examined the patient and the system has not, and spends her attention on the three she would not have thought of alone. Picture a biotech researcher staring at an anomalous result with seven candidate explanations. The system proposes experiments that would discriminate between them; she knows which of those experiments her lab can actually run by Friday, and that knowledge is the whole difference between a list and a plan. In each case the person supplies the thing the system lacks. The physician supplies the patient. The researcher supplies the lab.

Neither "replace" nor "assist" describes that. Replace is wrong on its face, since I was not replaced but changed. Assist is an understatement that misses the mechanism, because an assistant does part of your work and this did none of mine; it changed what I was capable of doing myself. The right word comes from chemistry. A catalyst lowers the barrier to a reaction and comes out the other side unchanged, with the whole transformation happening in the reactant, and so I have taken to calling what happened to me cognitive catalysis. Notice what that structure implies. In every one of these stories the human supplies what the system lacks: the domain, the question, the stubbornness, the desire to understand. A stronger catalyst does not make those contributions less valuable. It makes them decisive, because they become the only thing that distinguishes one outcome from another.

### Which jobs are safe? The same trap with a salary attached

The jobs question is the human-versus-machine question wearing a suit. Which jobs are safe, and which will disappear? Ask it and you can only get back lists, winners and losers sorted by occupation. The lists will be wrong in the way AGI dates are wrong and for the same reason. They assume the technology arrives with its uses already decided, so that the only thing left is to sort people into its path or out of it.

The record is unkind to the lists. When automated teller machines spread through American banking in the 1980s and 1990s, the obvious forecast was the end of the bank teller, and the forecast was wrong for thirty years. The number of tellers rose, because machines made branches cheaper to run, banks opened more branches, and tellers did different work in them. The technology did not decide that. People decided what to do with the branches, and the decision could have gone otherwise.

So the better question is not which existing jobs survive the machine but what new forms of work and collaboration we want to create with it. Every scenario earlier in this section implies work that did not exist five years ago: someone who designs the catalysis, someone who verifies, since a hundred patient experts are also a hundred confident ones, and someone who decides the ends, which no amount of technique supplies. None of these is a job title yet, and whether they become real work is not a question the technology will answer for us. That is the paradigm question hiding under the jobs question. Chapter 8 will argue that the line between human work and machine work has always been drawn by agreement rather than discovered, and Book II returns to knowledge work in detail.

That is the skill this section is for. When you hear a question framed as humans against machines, whether it arrives as an arrival date, a ranking, a consciousness debate, or a layoff forecast, stop and name the hidden premise. It is always some version of one axis, one finish line, one contest. Then put the question back in a form we can act on. Not "when will it match us?" but "what are we building together, and who decides?"

Drop the contest, though, and something else rushes in to fill the space. If it is not us against them, then surely the technology simply advances on its own and we adjust as best we can. That reflex is the second frame.

## The Technology Determinism Myth

### "Innovation equals progress"

The word "innovation" does moral work it has never been asked to justify. It names a change and grades the change in the same breath, and you can feel the grade built into the word by noticing that nobody says "a harmful innovation" without the sentence sounding slightly off. From there it is a short step to the assumption that sits under most writing about AI, usually without being stated: innovation is progress, progress is inevitable, and the only open question is how quickly we adapt.

It was not always so. For most of its life in English the word was an accusation. An innovator was someone who tampered with settled things, and "innovation" sat in the same family as heresy and sedition. Somewhere in the twentieth century the word flipped, keeping all of its old certainty and reversing the sign, so completely that almost nobody remembers there was a flip. A word that has carried opposite moral charges within living memory is not a word that should be allowed to settle arguments on its own.

I believed the modern version for most of my career, and I had the best possible excuse. The Prologue of this book opened in a Vancouver office in August 2019, with a screen showing the result of an A/B test. Two hundred and seven million dollars in revenue, attributable to a personalization algorithm my team had built. By any definition of innovation I knew at the time, it qualified. I remember the feeling precisely, and it was not triumph. It was the feeling of having answered, brilliantly, a question nobody had asked. Progress for whom? The objective function had never been given that question, so it had no opinion, and neither, I realized standing there, did I.

### Ignoring choice and design

What the determinist frame hides is this. Every system I have ever built embedded three choices that nobody in the room called choices: what to optimize, what data to trust, and what error to tolerate. Chapter 7 takes up the first two and Chapter 11 the third, so I will only point at them here. But I want to insist that they were choices, because the frame's whole trick is to make them look like facts about the technology.

Take the proudest moment of my thirteen years at Samsung. In 2009 my group redesigned a DRAM cell with the optimization platform I had built, and the head of the DRAM team said something I still quote. It was the first time in his career, he said, that he could say with certainty a design was the best possible one. He was right, and I am still proud of it. But "best" meant best under the objective I had been handed, performance and power and area in weights that someone had set, and the physics did not choose those weights. A meeting chose them, somewhere above my pay grade and well before I arrived. By the time the problem reached me the weights had hardened into requirements that nobody thought of as anyone's decision. That, most of the time, is what technological determinism is: not a property of the technology at all, but what a choice looks like after the people who made it have left the room.

Amazon taught the same lesson at a different scale. The personalization project that produced the number on the Vancouver screen did not work the first time. The first version failed, and what changed between the failure and the success was not mainly the algorithm. It was what we decided to count, which signals we trusted and which we discarded, and where we set the bar for calling a result real. Those decisions were made by a few people in a few meetings, and any of them could have gone differently. There is no version of the algorithm that worked in the abstract.

At Erudio Bio the choice is starker still, because it has a name in the statistics. A biomarker test can be tuned to miss fewer cancers at the cost of frightening more healthy people, or to frighten fewer healthy people at the cost of missing more cancers, and there is no setting of that dial that nature prefers. Someone sets it. Chapter 11 is about who, and on what authority, but I raise it here because it is the cleanest case I know of a technical parameter that is nothing but a choice about whose harm counts.

Put the cases together and the thing determinism deletes comes into focus. You can inspect everything about a system that is made of something: the silicon, the architecture, the data, the engineers who built it. What you cannot inspect, because it is not in the system, is what the system is for. Purposes are not found in objects. They are put there by someone, and when a system is described as though it simply did what it does, the purpose has not vanished. It has been hidden, and whoever hid it is usually the one it serves.

### Historical parallels

If the technology really did determine the outcome, the same technology would produce the same outcome everywhere, and it does not. Nuclear fission works identically in every country. Yet France built most of its electricity around it, Germany shut down its last reactor in 2023, and several countries with every bit of the necessary engineering capacity never built a plant at all. More telling still is what happened after Fukushima. Germany, whose reactors were nowhere near a tsunami, decided within months to leave the technology entirely. France, next door, with the same information, did not. The physics was constant and the societies were not. Whatever determined those outcomes, it was not the reactor.

The automobile tells the same story over a longer span. The car arrived in every rich country within the same two decades, and the cities those countries built around it could not be more different. The United States built highways through its city centers and moved its middle class to suburbs that cannot be lived in without a car. The Netherlands began down the same road and, in the early 1970s, after a campaign against the number of children killed in traffic, rebuilt its cities around the bicycle. Same machine, same decade, opposite cities. Anyone who tells you that a technology determines the shape of the society that adopts it has to explain Amsterdam.

Social media is the nearer parallel, because the choice is still visible if you know where to look. A feed sorted by what keeps people scrolling was not discovered inside the technology. It was chosen, in rooms I can picture because I have sat in their equivalents, and the choice was defensible on every metric those rooms were tracking. Engagement went up and revenue went up and the dashboards were green. The harms that followed, the polarization and the compulsive use and a public that could no longer agree on what had happened, arrived through exactly the mechanism that made the metrics go up. Nothing in the technology required that objective. Chapter 15 argues that we are now repeating the pattern with AI, step for step.

### Why the myth persists

There is an old move in which a person hands responsibility for a choice to an object so as not to have to own it. The driver says the car got away from him. The trader says the market moved. The engineer says the model decided. In each case something that a person did is attributed to a thing that cannot be blamed, and the person walks away lighter. Technological determinism is that move performed by an entire industry at once. The capability is treated as the agent so that the people deploying it need not be.

Which is why the myth persists: it relieves everyone. Engineers did not choose, they implemented. Executives did not choose, they responded to the market. Regulators could not have chosen, because the technology moved too fast. Run down the list and there is no one left in the room, and a frame in which nobody is responsible will never lack for sponsors. The question from the start of this chapter applies with full force. When a way of talking makes no one accountable, look for who is spared, because the people spared are the people who paid for the way of talking, whether or not they know it.

The skill, then, is to take any claim about what AI will do and split it in two. One part is trajectory, the genuinely new capability, and that part is real. The other part is choice, what someone decided to do with it, and that part is where the outcome lives. Then go looking for the three choice points. Who set the objective? Who picked the data? Who decided how much error was acceptable, and acceptable to whom? If you can find them, you have found the people to talk to. If you cannot find them, you are not looking at a fact about the technology. You are looking at a choice that someone has hidden, possibly even from themselves.

Determinism has two moods. In a good mood it promises abundance, cures, the end of drudgery; in a bad mood it predicts extinction. Both moods agree on the one thing that matters, which is that the outcome is coming regardless of what we do. They are one frame wearing two faces, and those two faces are the third frame.

## The Hype/Fear Binary

### The panel question

Go to any AI conference this year and wait, because it does not take long. Somewhere in the first panel a moderator will lean toward the microphone and ask the question the room has been waiting for: is AI safe, or is it dangerous? The audience sorts itself within minutes. You can watch it happen in the nods and the folded arms. And because I build these systems for a living, sooner or later someone turns to me and asks which side I am on.

The two sides are familiar enough to sketch, and each has serious people behind it. On one side is the story of abundance: AI will cure the diseases we could not cure, end the drudgery we could not escape, and deliver a plenty that makes the old scarcities look quaint. On the other side is the story of catastrophe: AI will empty the labor market, flood the public square with manufactured lies, concentrate power beyond any precedent, and, in the strong version, end us. In 2023 a one-sentence statement calling the risk of extinction from AI a global priority on the order of pandemics and nuclear war was signed by the heads of the leading laboratories.

Each side is persuasive for a reason. The abundance story points at things that are real: people are alive because of detectors like the one from earlier in this chapter. The catastrophe story points at things equally real: the disinformation engine exists, and the concentration of capability in a handful of firms is a plain fact. Neither side is lying about its evidence. Both are wrong about what the evidence is evidence of, and the way they are wrong is a good deal more instructive than either of them.

### The category error, again

The error is one we have met already, in a different costume. AI is a capability, not an agent with intentions. A knife in a chef's hand feeds a family, and the same knife in another hand takes a life. We do not convene panels on whether knives are safe; we ask who is holding one, in what setting, and under what rules. We have built an enormous apparatus of law and custom around exactly those questions without ever once needing to settle the moral status of cutlery.

Recall the two systems from earlier in this chapter, built on the same architecture, one flagging pancreatic cancer and the other manufacturing disinformation by the thousand. If "safe" or "dangerous" were a property of the architecture, those two systems could not both exist. Since they plainly do, the property must live somewhere else, in the people and institutions that chose what to build and where to point it. The same holds, with more force, for the general-purpose systems that most people now mean by AI, because a general-purpose system is precisely one whose purpose has not yet been chosen.

Which means that "AI is dangerous" and "AI is safe" are the same sleight of hand performed in opposite directions. Both locate the moral weight in the machine, and both let the humans leave the stage. The person who says the machine is dangerous and the person who says it is safe are agreeing about the one thing that matters, which is where to look, and they are both looking in the wrong place.

### Why the evasion is tempting: three reasons, three beneficiaries

Why is that evasion so tempting? I can think of three reasons, and each one has a beneficiary.

The first is psychological. If the danger is in the machine, then the problem is technical, and technical problems are the kind we know how to make progress on. We can benchmark them, fund them, and build teams around them. The alternative is to admit that the problem is us: our institutions, our incentives, our willingness to deploy what we have not understood. Human wisdom, unlike compute, does not double every eighteen months, and there is no benchmark for it. A technical problem is simply a more comfortable thing to have than a civilizational one.

The habit is old. The Luddites, who have become a byword for fearing machines, did not fear machines. They were skilled weavers who understood the new looms perfectly well, and what they objected to was who owned the looms, who captured the gains, and who bore the losses. The word survives as an insult because the story was retold with the machine as the villain and the ownership question removed. We are doing the same retelling now, and calling it the safety debate.

The second reason is political, and here the two frames split the spoils between them. Fear hands governments regulatory authority they would otherwise have to argue for, and it hands incumbents a barrier to entry, since compliance is cheap at scale and ruinous for a startup. In 2023 the chief executive of the most prominent AI laboratory sat before the United States Senate and asked to be licensed. It was reported as humility, and it was also the single most effective moat anyone in the industry had proposed. Fear hands researchers a funding line. Now consider what hype delivers. It raises capital in quantities without precedent for a technology this young, it justifies concentration as the price of progress, and it defers every hard question to a future that the hyped party fully expects to control. Fear and hope disagree about everything except the one thing that matters, which is who ends up holding the pen.

The third reason is conceptual. We are applying moral vocabulary built in the nineteenth century, for locomotives and bridges and medicines whose risks were bounded and local, to a technology whose reach is not bounded in that way. A bridge that fails kills the people on it. A system that shapes what a billion people see each morning has no such boundary, and rather than build new categories we have spent a decade arguing about which of the old ones to apply. "Safe" and "dangerous" are the old ones.

Now notice what the two stories have in common once you stop listening to their content. "AI safety," spoken often enough and by the right people, produces a world in which a small number of laboratories are the natural guardians of a danger that only they are equipped to measure. "AI abundance," spoken just as often, produces a world in which the same laboratories are the natural stewards of the coming plenty. The content of the two stories could not be more different. The cast is identical. When two opposed narratives install the same people in the same chairs, the opposition is not the point. The chairs are.

### The missing middle is an axis, not a midpoint

So what is in the middle? Not moderation. The middle is not "somewhat safe" or "dangerous but manageable," which are just the binary with the volume turned down, and anyone who answers the panel question with "it depends" has still accepted the question. The middle is a different axis entirely, and getting onto it takes a plain refusal to look away from the thing as it actually is.

The working rule I use is simple. Sort what people decide from what they do not, and spend your attention on the first list. The binary files AI, in its entirety, under the second: it is coming, it will save or destroy, and our role is to feel the appropriate emotion. Almost everything about these systems is in fact on the first list. What gets built, on what data, for whom, with what error rate, under what rules: every item has a person's name next to it, or could. The binary's deepest damage is that it teaches people to stand in front of a thing they could shape and feel about it instead.

And the thing as it actually is turns out to be sociotechnical. No AI system is deployed into a vacuum. It arrives inside an organization with incentives, a market with competitors, a legal regime with gaps, and a population with habits, and it behaves as all of those behave. The people who study industrial accidents concluded decades ago that the worst failures in complex systems live not in any component but in the interactions nobody designed and nobody is watching. Trying to make a system of many interacting agents safe by aligning each agent on its own is like trying to make a city safe by handing every citizen a handbook. Diagnosing the danger of an AI deployment by examining the algorithm is like diagnosing a patient by examining the left elbow. The elbow is real. It is just not where the illness is.

### Four harder questions

Once you are on that axis, the question "safe or dangerous" dissolves into four harder ones, and the binary survives partly by keeping them vague.

The first is institutional. What governance structures do we need for a general-purpose technology, and do they have teeth? It is easy to write a white paper; every ministry has one. What almost none of them has is enforcement capacity: inspectors who can read a system, penalties a large company would notice, and the budget to sustain any of it past the next election. A principle without enforcement is a press release, and Book III is the attempt to do better.

The second is concentration. Who gets to hold this capability, and how much of it? A law firm that wants a thousand more lawyers must find, hire, and pay a thousand people, which takes years and is visible to everyone. A firm with an AI legal system can deploy a thousand instances in the time it would take to interview one candidate, and nobody outside the firm need know. That asymmetry is new, and it favors whoever already has the systems, the data, and the compute. Chapter 10 and Book II take up what slows it, if anything does.

The third is meaning, and it is the one engineers are least comfortable with. What are humans for, once most cognitive labor becomes cheap? I have written elsewhere that "why do we live" is itself a wrong question, because it assumes meaning is a thing to be discovered, lying somewhere waiting, when meaning is something created by people who decide they want it. The same move applies here, and it is the hinge of this whole section. Safety is not discovered in a system any more than meaning is discovered in a life. It is created, by people who decide they want it and build the institutions to make it. The right question is whether we want safety enough to create it, and that question is answerable with a checkbox by no one.

The fourth is wisdom. Are we, as a civilization, mature enough to be trusted with this? Our institutions were designed for steam engines and telegraphs, for effects that arrived at the speed of a railway timetable, and they are now asked to govern effects that arrive at the speed of a software update. I do not know the answer. I know that it is a real question, that the binary prevents anyone from asking it, and that pretending we have answered it, in either direction, is the most dangerous thing in the room.

Two tests give the middle its working tools. The first: would you accept this design if you did not know which side of it you would be on, the patient or the radiologist, the rider or the driver, the person flagged or the person reviewing the flag? Most systems I have seen deployed would not survive that question, and most of the people who deployed them have never been asked it. The second: which decisions should not be delegated to a system, however accurate it is? The answer is not "none," whatever the accuracy numbers say, and Chapter 8 takes up which ones.

What to do, then, when someone offers you "safe or dangerous": decline the side. Name whom each side serves, which is usually the same people. Then move to the axis where the real questions live: what institutions, whose concentration, what human purpose, and how much wisdom. You will find that the room goes quieter, and that the people who were most certain a minute ago have the least to say, because the four questions require them to say where they stand, and the binary had been sparing them that.

One last reflex follows from that, and I will only name it here. If the answer to "safe or dangerous" is design and governance, the next question is who designs and who governs, and the usual answer, regulators, later, once they have caught up, is a fourth wrong question of its own. Chapter 14 takes it apart. Three frames are enough to show the pattern.

## Three Frames, One Structure

I promised at the start that by the end the three frames would look less like three mistakes and more like one, so here they are side by side.

**Table 6.1. Three frames of existing AI discourse**

| The frame | What it asks | What it hides | Who benefits from the hiding |
|---|---|---|---|
| Human vs. machine | When will AI match us? | What collaboration are we designing, and who decides? | Whoever profits from a contest, and from selling the finish line |
| Technology as destiny | What will AI do to us? | What are we choosing, and who chose? | Everyone who would rather not be responsible |
| Hype vs. fear | Is AI safe or dangerous? | Safe for whom, decided by whom? | Incumbents, regulators, and funders on both sides |

Read down the third column and the structure appears. Each frame takes the decisive choice and moves it somewhere no one can be held to account for it: into the machine, into history, into the future. Three frames making the same move is not three accidents. It is what a discourse looks like when it has been shaped, over years and without anyone needing to conspire, by the people it spares. Nobody designed the frames. They were selected, the way a river selects the stones that stay, by the simple fact that questions which threaten no one get asked more often than questions which do.

Read down the fourth column and something else appears, which is that the beneficiaries are not a cabal. They include governments and the companies governments regulate, the researchers who warn and the investors who hype, and what they share is an interest in the choice staying hidden, because every one of them is better positioned to make it quietly than to defend it in the open. That is why the frames are so durable. They are held up from every side at once.

For readers who build these systems, which includes most of the people I have given this talk to, the three skills have a practical form, and it fits on a single page of a design review. Next to the objective: who chose it, and who was not in the room. Next to the data: who it describes and who it leaves out. Next to the error rate: who set it and who bears it. None of those questions is technical, and the engineers who ask them are the ones whose systems are still running five years later.

I should say again what this chapter has not done. It has not offered a replacement. It has shown, three times, that the obvious question hides a choice and that the hiding has beneficiaries, and it has given you three habits for noticing when it happens. That is the necessary order. Frames do not fall to arguments. They fall when enough stops fitting inside them and someone offers a different frame in which the misfits turn out to be the normal case. This chapter was the pile of misfits. The chapters that follow are the offer, beginning in Chapter 7 with the claim that AI is not a technology to be controlled but a device that redistributes power and redesigns the choices available to everyone it touches. Chapter 9, the center of the book, asks why we reach for the wrong questions first, every time, and what a right question looks like.

> **Governance Insight** — *Jeff Lee and Hayden Song*
>
> The questions we ask determine the solutions we see. If we ask "When will AI be as smart as humans?" we design Turing tests. If we ask "How should AI reshape power?" we design governance structures. Current AI discourse asks the wrong questions because existing power structures benefit from those questions.

Back to the lecture hall, then, and to the briefing room. These days, when someone at the back stands up and asks whether AI will replace us, or how far behind we are, I answer with a question of my own: replace us at what, and chosen by whom? Behind whom, on a track laid out by whom, toward what? The room usually goes quiet for a moment. It is not an uncomfortable silence, or not only. It is the sound of a frame coming loose, and that silence is where the rest of this book lives.

