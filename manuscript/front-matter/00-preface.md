# Preface

In 2019, I was trying to understand how a universal basic income would affect poverty in the United States. Not the vibes-level version—"it would help a lot of people" or "it would cost too much"—but the precise version. How many families would cross the poverty line? Which families? What would it cost, net of reduced spending on existing programs? How would it interact with the Earned Income Tax Credit, SNAP, Medicaid, housing assistance?

I couldn't find the answer. Not because no one had modeled it, but because the models that could answer the question were locked inside government agencies and think tanks, built on proprietary data, and inaccessible to anyone outside those institutions. The Congressional Budget Office had models. The Tax Policy Center had models. The Joint Committee on Taxation had models. None of them were available for me to query with my specific question.

So I started building. First a scrappy research outfit called the UBI Center, running analyses on existing open-source tools. Then, with Nikhil Woodruff, PolicyEngine—an attempt to make the same kind of policy simulation available to anyone with a web browser. Enter your household details, change a policy parameter, see what happens. No expertise required. No paywall. No waiting for an analyst to run the numbers.

That work led to a series of questions I hadn't anticipated. If you can encode tax law as code, what else can you encode? If AI systems need accurate financial calculations and can't do them on their own, who builds the tools they call? If simulation can tell you what a policy does to people's wallets, can it also tell you what people think about it? And if you can simulate policies, opinions, and values—what does that mean for how society governs itself?

This book is my attempt to trace those questions from their origins to their implications.

---

## What this book is

This is a narrative about tools and the people who build them. It begins in 1957 with Guy Orcutt, an economist-engineer who imagined simulating society household by household, decades before the computers existed to do it. It moves through six decades of institutional microsimulation—mainframes at the Urban Institute, proprietary models at the Congressional Budget Office, the quiet revolution of open-source policy tools in Europe and the United States. It arrives at the present moment, where AI systems need deterministic tools for financial calculations, where open-source simulation is becoming public infrastructure, and where the boundaries of what we can simulate are expanding in directions that raise hard questions about democracy, values, and what it means to model a society.

Along the way, I describe projects I've built or helped build—PolicyEngine, HiveSight, Democrasim, Cosilico, the Rules Foundation. I try to be honest about what works, what doesn't, and what remains aspiration rather than accomplishment. Some chapters describe validated systems with real users. Others describe prototypes. One chapter describes infrastructure that doesn't yet exist. I label the differences clearly, because the distinction between "this works" and "this might work someday" matters.

## What this book is not

This is not a textbook. I won't teach you microsimulation methodology, and the technical details I include are meant to illuminate ideas, not to serve as documentation. If you want to learn how to build a tax-benefit model, the references will point you to better sources.

This is not a memoir, though my own path through this work provides the connective tissue. I include personal experience where it illuminates the ideas and omit it where it doesn't. The story of microsimulation is bigger than any one person's involvement.

This is not a manifesto. I have views—about open source, about democratic access to information, about how AI should handle policy questions—but I try to present them alongside the strongest counterarguments I can find. The chapters on silicon sampling and democratic simulation, in particular, are structured around the tensions and limitations of the ideas, not as advocacy.

And this is not finished. I'm writing it while the work it describes is ongoing. PolicyEngine continues to evolve. The Rules Foundation is encoding new statutes. Cosilico is still early. The research directions in Part III—simulating opinion, democracy, values—are genuinely speculative. I think there's value in describing the landscape as it exists, including the parts that are still being built. But readers should understand that some of what I describe will look different in two years.

## Who this book is for

I've tried to write for three audiences simultaneously, which probably means I've imperfectly served all three.

**Policy people** who want to understand how computational tools are changing policy analysis. You don't need to know how to code. I explain the technical concepts through stories and examples, and the details that matter—how a tax-benefit model works, what microsimulation actually does, why AI can't just learn tax law—are explained in plain language.

**Technologists** who are building AI systems, fintech applications, or data infrastructure and want to understand the policy domain. You'll find the technical architecture discussions relevant, and the policy context will help you understand why this domain is harder than it looks.

**Curious readers** who follow the intersection of technology and governance. If you've wondered why AI gets tax questions wrong, why government budget models are secret, or what it would mean to simulate a society—this book is an attempt to answer those questions accessibly.

## How to read this book

The book is organized in three parts, and they build on each other but can be read somewhat independently.

**Part I: Origins** is history. It covers the intellectual tradition of microsimulation, from Orcutt's insight through the institutional models that shaped decades of policy analysis. If you want to understand where these tools came from and why they matter, start here.

**Part II: Building** is about the present. It describes the open-source tools that are making policy simulation public infrastructure—PolicyEngine's household and society views, the role AI is beginning to play, and the infrastructure gap that led me to explore building Cosilico and the Rules Foundation.

**Part III: Research directions** is about the future, and it's the most speculative section. It covers uncertainty quantification, silicon sampling for opinion research, simulating democratic processes, and the question of whether simulation can help with AI alignment. These chapters are clearly labeled as research directions rather than established work.

If you're impatient, you could read the introduction, skip to Part II for the practical story, and dip into Part III for the ideas that interest you. If you have time, the history in Part I provides context that makes everything else richer.

---

I started this project because I believed—and still believe—that the tools we use to understand society shape the decisions we make about it. When those tools are locked inside institutions, the understanding is locked too. When they're open, transparent, and accessible, more people can participate in the conversation about what policies we should adopt and why.

That's an optimistic view. Whether it survives contact with the evidence is something you can judge for yourself.

Max Ghenis
San Francisco, 2026
