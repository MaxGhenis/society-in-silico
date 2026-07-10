# Preface

In 2019, I was trying to understand how a universal basic income would affect poverty in the United States. Not the vibes-level version—"it would help a lot of people" or "it would cost too much"—but the precise version. How many families would cross the poverty line? Which families? What would it cost, net of reduced spending on existing programs? A $1,000-a-month basic income runs to roughly $3 trillion a year; the interesting questions all live in how you pay for it, and in how it interacts with the Earned Income Tax Credit, SNAP, Medicaid, and housing assistance.

I couldn't find the answer. Not because no one had modeled it, but because the models that could answer the question were locked inside government agencies and think tanks, built on confidential data, and inaccessible to anyone outside those institutions. The Congressional Budget Office had models. The Tax Policy Center had models. The Joint Committee on Taxation had models. None of them were available for me to query with my specific question.

So I started building. First a scrappy research outfit called the UBI Center, running analyses on existing open-source tools. Then, with Nikhil Woodruff, PolicyEngine—an attempt to make the same kind of policy simulation available to anyone with a web browser.^[A disclosure that is also, I think, part of the story: as of July 2026, Nikhil serves in the UK government at 10 Downing Street. [VERIFY with Nikhil: role wording] Where this book discusses UK institutions evaluating tools he helped build, read it with that in mind.] Enter your household details, change a policy parameter, see what happens. No expertise required. No paywall. No waiting for an analyst to run the numbers.

That work led to a series of questions I hadn't anticipated. If you can encode tax law as code, what else can you encode? If AI systems need accurate financial calculations and can't do them on their own, who builds the tools they call? If simulation can tell you what a policy does to people's wallets, can it also tell you what people think about it? And if you can simulate policies, opinions, and values—what does that mean for how society governs itself?

This book is my attempt to trace those questions from their origins to their implications.

---

## What this book is

This is a narrative about tools and the people who build them. It begins in 1957 with Guy Orcutt, an economist-engineer who imagined simulating society household by household, decades before the computers existed to do it. It moves through six decades of institutional microsimulation—mainframes at the Urban Institute, proprietary models at the Congressional Budget Office, the quiet revolution of open-source policy tools in Europe and the United States. It arrives at the present moment, where AI agents write and verify the code that once took institutions years to build, where open simulation is becoming public infrastructure, and where the boundaries of what we can simulate are expanding in directions that raise hard questions about democracy, values, and what it means to model a society.

Along the way, I describe projects I've built or helped build—PolicyEngine, HiveSight, Democrasim, the Axiom Foundation, and the Thesis Institute. I try to be honest about what works, what doesn't, and what remains aspiration rather than accomplishment. The honest accounting turned out to be a moving target. A chapter drafted in 2025 as a sketch of infrastructure that didn't yet exist had to be rewritten in 2026 as a field report on infrastructure that does—law encoded by AI agents and checked, line by line, against the models governments already trust. Other parts remain exactly as speculative as they were. I label the difference throughout, because the distinction between "this works," "this is early," and "this might work someday" is the book's whole currency—and the speed at which things moved between those categories is itself part of the story.

## What this book is not

This is not a textbook. I won't teach you microsimulation methodology, and the technical details I include are meant to illuminate ideas, not to serve as documentation. If you want to learn how to build a tax-benefit model, the references will point you to better sources.

This is not a memoir, though my own path through this work provides the connective tissue. I include personal experience where it illuminates the ideas and omit it where it doesn't. The story of microsimulation is bigger than any one person's involvement.

This is not a manifesto. I have views—about open source, about democratic access to information, about how AI should handle policy questions—but I try to present them alongside the strongest counterarguments I can find. The chapters on simulated opinion and simulated democracy, in particular, are structured around the tensions and limitations of the ideas, not as advocacy.

And this is not finished. I'm writing while the work is ongoing. The Axiom Foundation launches publicly this summer; the Thesis Institute follows in the fall; the forecasts its scoreboard publishes will take years to grade themselves against reality, and as of this writing not one has resolved. The research directions in the later chapters—simulating opinion, democracy, values—are genuinely speculative, and I say so where they are. Readers should expect that some of what I describe will look different in two years. Between the first draft and this one, it already does.

## Who this book is for

I've written for three readers, and any one lens is enough.

**Policy people** who want to understand how computational tools are changing policy analysis. You don't need to know how to code. I explain the technical concepts through stories and examples, and the details that matter—how a tax-benefit model works, what microsimulation actually does, why AI can't just learn tax law—are explained in plain language.

**Technologists** who are building AI systems, fintech applications, or data infrastructure and want to understand the policy domain. You'll find the architecture discussions relevant, and the policy context will help you understand why this domain is harder than it looks.

**Curious readers** who follow the intersection of technology and governance. If you've wondered why AI gets tax questions wrong, why government budget models are secret, or what it would mean to simulate a society—this book is an attempt to answer those questions accessibly.

## How to read this book

The book runs in five parts, and they build on each other but tolerate skipping.

**Part I: The closed stack** is history—how government built an analytic machinery the public couldn't see, from Orcutt's 1957 vision through the tax model wars, ending with the question that disciplines everything after it: how would you know whether any of these models is right?

**Part II: The open engine** is the PolicyEngine story—proof that the closed stack could be rebuilt in public, what the engine shows one household and a whole country, and the three ingredients every such model must solve.

**Part III: The agent turn** is the new heart of the book: why AI systems need deterministic policy tools, how AI agents came to write verified law-as-code at scale, how you trust machine-encoded law, and what happened when the method reached countries that never had public models at all.

**Part IV: The prediction pole** crosses from calculation to forecasting—the uncertainty that point estimates hide, the scoreboard being built to price it honestly, and what large language models actually add to opinion research once you benchmark them.

**Part V: The horizon** is the speculative edge—simulated democracy, simulated values—clearly labeled, and the return to the fork in the road the introduction opens.

If you're impatient, read the introduction, then Part III, and dip into Part V for the ideas that interest you. If you have time, the history in Part I makes everything else richer.

---

I started this project because I believed—and still believe—that the tools we use to understand society shape the decisions we make about it. When those tools are locked inside institutions, the understanding is locked too. When they're open, transparent, and accessible, more people can participate in the conversation about what policies we should adopt and why.

That's an optimistic view. Whether it survives contact with the evidence is something you can judge for yourself.

Max Ghenis
Washington, DC, 2026
