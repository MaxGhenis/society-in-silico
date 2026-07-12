# Preface

In 2019 I wanted a number nobody would give me. The question was simple to state: if the United States paid every adult a basic income, how many families would that pull over the poverty line, and what would it cost once you netted out the programs it replaced? Congress had models that could answer it — the Congressional Budget Office's, the Joint Committee on Taxation's. So did the Treasury, and, outside government, the Tax Policy Center. I could read their reports. I could not ask their models my question, because the models lived behind institutional walls, most ran on confidential data, and all answered only to their owners.

So I built. First a scrappy research shop called the UBI Center, which ran analyses on the open-source tools that existed. Then, with Nikhil Woodruff — a college student I found on a subreddit, who turned out to pair real economics with real engineering — PolicyEngine: policy simulation for anyone with a web browser.^[A disclosure that doubles as a plot point: as of July 2026, Nikhil serves in the UK government at 10 Downing Street. [VERIFY with Nikhil: role wording] When this book describes British institutions evaluating tools he helped build, read it knowing where he sits now.] Type in your household, move a policy lever, watch your taxes and benefits recompute. No credentials, no paywall, no waiting.

Building it raised questions I had not planned to spend my thirties on. If you can encode tax law, what else can you encode? When an AI assistant answers a benefits question — and it will, because that is where people now ask — who builds the calculator it should be calling instead of guessing? If simulation can say what a policy does to a family's budget, can it say what the public thinks about it? And if machines can hold the rules, the people, and the predictions all at once, what keeps any of it honest?

That last question runs the book. My answer, stated up front so you can hold me to it: a simulation deserves your attention only where you can check it against something real — a statute, a census total, an official number that arrives later and grades the forecast. Everything I describe here either passes that test, fails it in the open, or gets labeled as the speculation it is.

## What this book is

A story about tools and the people who built them. It starts in 1957, when an economist named Guy Orcutt proposed simulating a nation household by household, decades before computers could. It runs through the era when such models existed but belonged to institutions — mainframes at the Urban Institute, black boxes at the CBO — and through the open-source turn that put them in browsers. It ends somewhere I did not expect when I started writing: AI agents encoding entire countries' tax codes in a day and proving their work against the reference models governments already trust.

That ending rearranged the book under me. A chapter I drafted in 2025 described infrastructure that did not exist and said so plainly. By mid-2026 the infrastructure existed, and the chapter had to become a field report. I have kept the labels current throughout — this works, this is early, this is speculation — because the boundary between them is the book's real subject, and because the speed at which things crossed it is the story.

## What this book is not

Not a textbook; when I include technical detail, it is there to make an idea land, and the references point to proper treatments. Not a memoir; my path supplies connective tissue, and the story is bigger than it. Not a manifesto; I hold views and argue them, but the chapters on simulated opinion and simulated democracy give the strongest counterarguments I could find, because those ideas deserve adversaries.

And not finished. The Axiom Foundation launches this summer. The Thesis Institute follows in the fall, and its first forecasts will take months and years to grade — as I write, not one has resolved. Some of what you read here will look different in two years. Between my first draft and this one, it already does.

## Who this book is for

Three readers, any one lens enough. Policy people who want to know how computation is changing their trade, with no code required. Technologists building AI, fintech, or data systems who need to understand why this domain punishes shortcuts. And anyone who has wondered why the chatbot gets tax questions wrong, why budget models are secret, or what it would mean to run society's experiments in silicon before running them on people.

## How to read it

Five parts. Part I is history: how government built an analytic machine the public could not inspect, and how you would even know whether such a machine is right. Part II is PolicyEngine: rebuilding that machine in the open, for one household and for a country. Part III is the turn everything else follows from: AI agents writing verified law-as-code at scale, the discipline that makes their work trustworthy, and what happened when the method reached countries that never had public models at all. Part IV crosses from calculation to prediction — the uncertainty that point estimates hide, and a public scoreboard that waits for reality to grade it. Part V walks to the speculative edge, simulated democracy and simulated values, and returns to the choice the introduction opens.

Impatient readers: introduction, then Part III, then whatever pulls you. The history repays the time, but the book tolerates skipping.

---

I wrote this book because the tools we use to understand society decide what we can see about it, and for fifty years the best tools belonged to the few institutions that could afford them. That era is ending. What replaces it — open machinery anyone can inspect and check, or closed machinery with a friendlier interface — is being decided now, in code, in procurement contracts, and in choices that look technical but are not.

You can judge for yourself whether the open path holds up. The evidence is all here, marked with exactly how much I trust it.

Max Ghenis
Washington, DC, 2026
