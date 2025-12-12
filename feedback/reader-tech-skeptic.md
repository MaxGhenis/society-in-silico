## Reader Review: Tech Skeptic (Priya)

### Technical Assessment

Mixed. The author clearly understands computational policy modeling—the references to microsimulation, vectorized computation, and historical systems like DYNASIM suggest real domain expertise. But the AI section feels… 2022? The GPT-4 tax accuracy argument (67% on true/false questions) is being used to dismiss LLMs entirely, which shows a misunderstanding of how these systems work and where they're heading.

The Westworld hook is engaging but reveals something: the author sees "deterministic models" as the safe democratic alternative to opaque AI. That's a false dichotomy. Deterministic doesn't mean interpretable—I've seen 100K-line rules engines that are effectively black boxes. And probabilistic doesn't mean unaccountable—we have entire subfields (XAI, mechanistic interpretability) working on this.

Technical credibility: **6/10**. Strong on policy simulation, weak on modern ML capabilities and trajectory.

### The AI Argument

**Fair points:**
- GPT-4 does hallucinate on structured tasks (though 67% on tax law with full IRC context is actually impressive given no fine-tuning)
- Current LLMs struggle with deterministic computation (arithmetic, tax calculations, exact rule application)
- Policy decisions have real stakes; you can't hand-wave errors with "it's usually right"
- There's value in reproducible, auditable calculations

**Weak points:**
- Treating GPT-4's base performance as the ceiling for AI capabilities
- Ignoring the entire toolformer/agent paradigm—LLMs + deterministic tools
- Not engaging with fine-tuning (a specialized tax model would do much better than general GPT-4)
- Missing RAG entirely (retrieval-augmented generation could ground responses in actual tax code)
- The "AI hallucinates eligibility rules" line implies LLMs are the only AI approach, when ML includes everything from gradient boosting to transformers
- No mention of verification techniques (e.g., having models explain their reasoning, cross-checking with symbolic systems)

The paper cited (Blair-Stanek et al. 2023) had GPT-4 answer true/false questions with the full Internal Revenue Code as context. That's a pure reading comprehension task, not even using the model's strengths. Of course it struggled—transformers aren't optimized for exact legal text matching. But that doesn't mean AI can't help with tax policy.

### "Why Not Just Use ML?" Test

**Did they convince me deterministic matters?**

Not really. The argument boils down to: "LLMs hallucinate, therefore we need deterministic rules engines." But this ignores:

1. **Hybrid architectures**: Why not LLM interfaces that call deterministic calculators? The best systems already do this (think ChatGPT with Code Interpreter, or Anthropic's tool use). You get natural language interaction + reliable computation.

2. **The specification problem**: Deterministic models are only as good as their rules. Tax code has ambiguities, edge cases, conflicting interpretations. Someone has to encode that—and that human judgment is where errors creep in. At least with ML you can update on new data.

3. **Scalability**: Rules engines require manual encoding of every jurisdiction, every policy change. Fine-tuned models can generalize across similar policy domains. Which approach scales to 50 states + federal + future policy regimes?

4. **The open source argument**: I actually buy that transparency matters for democratic policy analysis. But why does "transparent" = "deterministic code"? You can open-source training data, model weights, inference code. We do this in ML all the time (see: LLaMA, Stable Diffusion, etc.).

The author hasn't explained why deterministic simulation is fundamentally better than probabilistic prediction + verification. They've just shown that unaugmented GPT-4 isn't good enough—which everyone in AI already knows.

**What's missing**: Engagement with state-of-the-art. The introduction reads like it was written before:
- Toolformer (2023) - LLMs that learn to use external tools
- Function calling became standard in all major APIs (2023-2024)
- Constitutional AI and RLHF for reducing hallucinations
- Agent frameworks (AutoGPT, LangChain, etc.) that combine LLMs with deterministic tools
- Advances in formal verification for neural networks

### Where I Might Be Wrong

Steel-manning the deterministic argument:

**The auditability point is actually strong.** When a caseworker denies someone benefits, or Congress debates a tax bill, you need to trace the logic. "The model said so" (probabilistic) is legitimately worse than "here's the exact rule and calculation" (deterministic). Democratic accountability requires explanations, not just predictions.

**Reproducibility matters for science and policy.** If two researchers run the same policy simulation, they should get identical results. Stochastic models introduce variance that complicates comparison. For academic research and legislative analysis, determinism has real value.

**The "who builds them" question is interesting.** Open source rules engines invite collaboration—anyone can propose a PR to fix a bug in the tax code implementation. Training data for ML models is messier: Who curates it? What biases does it encode? There's something democratically appealing about "the model is literally the law, encoded."

**Maybe we're at a transition point.** Right now (2025), deterministic tools might be more reliable for policy calculation than LLMs. But the author is writing a book that will be read for years. If the argument is "deterministic tools matter in 2025," fine. If it's "deterministic tools will always matter," that's much harder to defend as AI capabilities improve.

**The institutional inertia point is unexplored but real.** Even if LLMs eventually surpass rules engines, governments move slowly. We'll have legacy systems for decades. Making those systems open and accessible could be valuable regardless of where AI goes.

### What Would Convince Me

I'd update toward "deterministic simulation tools matter long-term" if I saw:

1. **Proof that hybrid approaches fail**: Show me that LLM + deterministic calculator architectures don't work. Because right now, that seems like the obvious solution: natural language interface, symbolic computation backend. If there's a fundamental reason this fails, I want to see it.

2. **Evidence of fundamental ML limitations**: Not "GPT-4 gets 67% on tax questions" but "here's a theoretical reason transformers/neural nets can't learn exact rule application even with unlimited data and compute." I doubt this exists—we have universal approximation theorems, and ML systems already do exact computation in narrow domains.

3. **Comparative accuracy studies**: Take a complex policy question. Compare:
   - Human policy analyst
   - Traditional rules engine (like PolicyEngine)
   - Fine-tuned LLM (GPT-4 + tax code training data)
   - Hybrid (LLM + rules engine)

   If the rules engine consistently outperforms sophisticated ML approaches, that's real evidence. The GPT-4 baseline test isn't enough.

4. **Democratic participation metrics**: The author claims open source simulation tools are better for democracy than AI. Show me. How many people actually contribute to PolicyEngine vs how many use Claude/ChatGPT for policy questions? If the goal is democratization, which approach gets more people engaged?

5. **Failure cases for verification**: I currently believe you can verify LLM outputs (e.g., have the model explain its reasoning, cross-check against symbolic rules, use multiple models and check consensus). If there are policy domains where verification is provably insufficient, that would change my mind.

6. **The interpretability ceiling**: If there's evidence that ML systems will never be as interpretable as rules engines—not just "current systems aren't" but "fundamental limits exist"—that matters. Though I'd note that 100K lines of spaghetti tax code isn't exactly interpretable either.

**What would really convince me**: A chapter that engages seriously with AI trajectory. Not "GPT-4 can't do this" but "here's why even GPT-7 won't be able to do this" or better yet "here's why we want deterministic tools even if AI can match them." The second argument is more defensible: democracy might require inspectable logic regardless of capability.

---

**Bottom line**: I'm sympathetic to open-source policy tools. I'm skeptical that "deterministic vs probabilistic" is the right frame. The introduction sets up a straw man (unaugmented GPT-4) and doesn't engage with how AI is actually being deployed (agents + tools, fine-tuning, verification, hybrid systems).

If the book is "why policy simulation tools should be open source," I'm interested. If it's "why deterministic beats probabilistic," I need much stronger arguments. Right now it reads like someone who built a rules engine and is defensive about LLMs—understandable, but not convincing to someone who's seen what modern ML can do.

**Recommended reading for the author**:
- Toolformer: Language Models Can Teach Themselves to Use Tools (2023)
- Constitutional AI papers from Anthropic
- Agent frameworks that combine LLMs + symbolic reasoning
- XAI literature on making ML interpretable

The book could be much stronger if it positioned deterministic tools as *complementary* to AI rather than *opposed* to it. That's the future I see: LLMs that can explain policy in natural language, backed by deterministic calculators that ensure accuracy. Why not build toward that?
