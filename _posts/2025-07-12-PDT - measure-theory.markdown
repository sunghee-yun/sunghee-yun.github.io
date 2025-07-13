---
permalink: /math/measure-theory
title: The Revolution that Transformed Analysis Forever &ndash; Lebesgue's Gift to Modern Analysis
date: Sat Jul 12 04:59:40 PDT 2025
last_modified_at: Sun Jul 13 02:42:04 PDT 2025
categories:
 - blog
tags:
 - math
 - measure theory
 - Lebesgue integral
 - real analysis
 - Henri Lebesgue
 - slides
 - document
usemathjax: true
toc: true
toc_label: "&nbsp;Table of Contents"
toc_icon: "fa-solid fa-list"
toc_sticky: true
---

posted: {{ page.date| date: "%d-%b-%Y" }}
&amp;
updated: {{ page.last_modified_at| date: "%d-%b-%Y" }}
{: .notice--primary}

<blockquote>
<a href="#birth of measure theory">
&hellip; few people could ever imagine how thrilled I was when learning about the moment when the French mathematician, Lebesgue, won
the race of inventing (or finding) a new way to overcome the limits of Riemann integral in 1912,
which let all human race witness the birth of measure theory!</a>
</blockquote>

<blockquote>
<a href="#Lebesgue's breakthrough">Lebesgue's breakthrough came from a radical change in how we think about integration. Instead of partitioning the domain (as Riemann did), Lebesgue partitioned the range of the function and asked: "What is the measure of the set where the function takes values in each interval?"</a>
</blockquote>

<blockquote>
<a href="#genius of Lebesgue's theory">
The true genius of Lebesgue's theory lies not just in its technical innovations, but in its conceptual foundations.
</a>
</blockquote>

<blockquote>
<a href="#highlight-conceptual-revolution">The creation of measure theory wasn't just a mathematical advancement&mdash;it was a conceptual revolution that fundamentally changed how we understand the very notion of <i>size</i> and <i>integration</i> in mathematics.
And in revealing these universal principles, Lebesgue showed us that the search for mathematical truth often leads to insights far deeper and more beautiful than we initially imagined.</a>
</blockquote>

<blockquote>
<a href="#question-most-basic-assumptions">Sometimes the biggest breakthroughs come from examining our most basic assumptions.</a>
</blockquote>

<blockquote>
<a href="#find-right-abstract">The power of mathematics often lies in finding the right abstract framework.</a>
</blockquote>

<blockquote>
<a href="#beautiful-examples">Lebesgue's measure theory stands as one of the most beautiful examples
of how the search for mathematical truth leads to insights that transform our understanding not just of specific problems,
but of the fundamental nature of mathematical reasoning itself.</a>
</blockquote>

<!--blockquote>
Lebesgue's integral doesn't just extend Riemann's&mdash;it reveals the deeper structural principles that make integration possible at all.
</blockquote-->

<!--# NotebookLM Podcasts-->

<!--h2>based on this blog</h2-->

<!--audio id="podcast-1" controls>
	<source type="audio/wav" src="">
	Your browser does not support this shorter audio element.
</audio-->

<!--h2>based on Measure Theory Codex</h2-->

<!--audio id="podcast-slides-1" controls>
	<source type="audio/wav" src="">
	Your browser does not support this shorter audio element.
</audio-->

# Parent blog post

{% assign math_landscape = site.posts | where: "permalink", "/math/landscape" | first %}
- [{{ math_landscape.title }}]({{ math_landscape.url }})

# Sibling blog posts

{% assign inequalities = site.posts | where: "permalink", "/math/inequalities" | first %}
{% assign abstract_algebra = site.posts | where: "permalink", "/math/abstract-algebra" | first %}

- [{{ inequalities.title }}]({{ inequalities.url }})
- [{{ abstract_algebra.title }}]({{ abstract_algebra.url }})

# Measure Theory Codex {#measure-theory-codex}

- [Searching for Universal Truths - Measure Theory](/resource/fun math/fun_math_mtheory.pdf) (updated on 12-Jul-2025)

# Mathematical Race of 1902

There are moments in mathematical history when a single insight transforms our understanding so completely that we can speak of "before" and "after." The year 1902 marked one such watershed moment when [Henri Léon Lebesgue](https://en.wikipedia.org/wiki/Henri_Lebesgue), then just 27 years old, presented his revolutionary theory of integration to the mathematical world.

As I mentioned in my broader exploration of [{{ math_landscape.title }}]({{ math_landscape.url }}),
<span id="birth of measure theory">few people could ever imagine how thrilled I was when learning about this pivotal moment—when Lebesgue won the race of inventing (or finding) a new way to overcome the limits of Riemann integration, letting all humanity witness the birth of measure theory!</span>

But this wasn't just another mathematical advancement. Lebesgue's work represented a fundamental reconceptualization of what it means to measure and integrate, revealing universal principles that continue to shape modern analysis, probability theory, and our understanding of mathematical structure itself.

# Crisis that Demanded Revolution

## Limitation of Riemann integration

By the late 19th century, mathematicians had encountered a fundamental problem that Riemann integration simply couldn't resolve. Consider the characteristic function of rational numbers on the interval [0,1].

$$\chi_Q(x) = \begin{cases}
1 & \text{if } x \in \mathbb{Q} \\
0 & \text{if } x \notin \mathbb{Q}
\end{cases}$$

This function, while perfectly well-defined and seemingly simple, was not Riemann integrable. When we attempt to compute Riemann sums, every interval contains both rational and irrational numbers, making the upper and lower sums stubbornly different because

- The lower sum is 0 since the infimum on any interval is 0.
- The upper sum is 1 since the supremum on any interval is 1.

Since $$\sup \text{(lower sums)} = 0 \neq 1 = \inf \text{(upper sums)}$$, the Riemann integral simply doesn't exist for this function.

## Deeper problem

But mathematicians recognized something profound -
since rational numbers are countable while irrational numbers are uncountable,
or if I use my own invented expression that I enjoy using a lot,
which is a mathematically totally non-strict expression,
since there exist infinite times more irrational numbers than rational numbers,
intuitively we should have

$$\int_0^1 \chi_Q(x) \, dx = 0 \quad \text{and} \quad \int_0^1 (1-\chi_Q(x)) \, dx = 1$$

The rational numbers, being countable, should contribute "zero measure" to the integral, while the irrational numbers should contribute the full measure of the interval.

This intuition pointed toward a deeper mathematical truth &ndash; we needed a notion of "measure" that could distinguish between countable and uncountable sets, and an integration theory built on this foundation.

# Lebesgue's Revolutionary Insight

## Fundamental shift in perspective

<span id="Lebesgue's breakthrough">Lebesgue's breakthrough came from a radical change in how we think about integration. Instead of partitioning the domain (as Riemann did), Lebesgue partitioned the range of the function and asked: "What is the measure of the set where the function takes values in each interval?"</span>

This shift from "horizontal slicing" (domain partition) to "vertical slicing" (range partition) was more than a technical innovation—it was a conceptual revolution that revealed the true structure underlying integration.

## Building the foundation - outer measure

Lebesgue began by constructing what we now call **outer measure** $$\mu^\ast:\mathcal{P}(\mathbb{R})\to\mathbb{R}_+$$. For any set $$E \subset \mathbb{R}$$, he defined

$$\mu^*(E) = \inf\left\{\sum_{i=1}^{\infty} l(I_i) : E \subset \bigcup_{i=1}^{\infty} I_i\right\}$$

where the infimum is taken over all countable collections of open intervals $$\{I_i\}$$ that cover $$E$$, and $$l(I_i)$$ denotes the length of interval $$I_i$$.

This definition captures our intuitive notion of "size" while $$\mu$$ being
- **well-defined** - for every subset of $$\mathbb{R}$$
- **monotonic** - $$A \subset B \Rightarrow \mu^*(A) \leq \mu^*(B)$$
- **countably subadditive** - $$\mu^*\left(\bigcup_{i=1}^{\infty} A_i\right) \leq \sum_{i=1}^{\infty} \mu^*(A_i)$$

## Crucial insight - measurable sets

The genius of Lebesgue's approach was recognizing that not all sets should be treated equally.
He defined a set $$E$$ to be **measurable** if it satisfies Carathéodory's criterion,
*i.e.*,

$$\mu^*(A) = \mu^*(A \cap E) + \mu^*(A \cap E^c)$$

for every subset $$A \subset \mathbb{R}$$.

This condition ensures that measurable sets *split* other sets additively with respect to outer measure—a fundamental property that makes measure theory work.

## Miraculous result

The collection of measurable sets forms a $$\sigma$$-algebra, and when we restrict outer measure to measurable sets, we obtain **Lebesgue measure** $$\mu$$&mdash;a measure that is

1. **countably additive** on disjoint measurable sets
2. **translation invariant**
3. **extends length** for intervals
4. **assigns measure zero** to countable sets

This resolved the crisis that motivated the theory,
*i.e.*,

- $$\mu(\mathbb{Q} \cap [0,1]) = 0$$ (rationals have measure zero)
<!--- $$\mu((\mathbb{R} \setminus \mathbb{Q}) \cap [0,1]) = 1$$ (irrationals have full measure)-->
- $$\mu([0,1] \setminus \mathbb{Q}) = 1$$ (irrationals have full measure)

# The Lebesgue Integral - Integration Transformed

## From simple to general

With Lebesgue measure in hand, Lebesgue constructed his integral through a natural progression.

<h3>step 1 - simple functions</h3>
For a *simple* function $$\phi = \sum_{i=1}^n a_i \chi_{A_i}$$ where $$A_i$$ are disjoint measurable sets,
the Lebesgue integral is defined by

$$\int \phi \, d\mu = \sum_{i=1}^n a_i \mu(A_i).$$

<h3>step 2 - nonnegative functions</h3>
For a nonnegative measurable function $$f$$,
the Lebesgue integral is defined by

$$\int f \, d\mu = \sup\left\{\left.\int \phi \, d\mu \right| \phi \text{ simple}, \phi \leq f\right\}.$$

<h3>step 3 - general functions</h3>
For any measurable function $$f = f^+ - f^-$$ where $$f^+ = \max(f,0)$$ and $$f^- = \max(-f,0)$$,
the Lebesgue integral is defined by

$$\int f \, d\mu = \int f^+ \, d\mu - \int f^- \, d\mu.$$

provided both integrals on the right are finite.

## Revolutionary consequences

This construction immediately yielded profound results that were impossible in the Riemann framework.

<h3>The monotone convergence theorem</h3>
For a sequence of nonnegative measurable functions $$f_n \uparrow f$$

$$\int f \, d\mu = \lim_{n \to \infty} \int f_n \, d\mu.$$

<h3>The dominated convergence theorem</h3>
If $$f_n \to f$$ almost everywhere and $$|f_n| \leq g$$ where $$g$$ is integrable

$$\int f \, d\mu = \lim_{n \to \infty} \int f_n \, d\mu.$$

These theorems provide the foundation for modern analysis by giving precise conditions under which we can interchange limits and integration—something that was often problematic in the Riemann theory.

# Conceptual Revolution

## What Made Lebesgue's Approach Revolutionary?

<div id="genius of Lebesgue's theory">
The true genius of Lebesgue's theory lies not just in its technical innovations, but in its conceptual foundations.
</div>

<h3>Measure before integration</h3>
Lebesgue recognized that integration should be built on a prior theory of measure. This insight revealed that integration is fundamentally about weighted sums over measurable sets, not just limits of Riemann sums.

<h3>Focus on sets of measure zero</h3>
The concept of *almost everywhere* became central to analysis. Properties that hold except on sets of measure zero are treated as essentially universal—a profound shift that simplified and unified many analytical arguments.

<h3>Structural approach</h3>
Rather than defining integration algorithmically (as with Riemann sums), Lebesgue took a structural approach, defining integration through suprema over approximating simple functions. This revealed integration as a natural extension of basic arithmetic to infinite processes.

<h3>Universal framework</h3>
Lebesgue's approach naturally generalizes beyond the real line to abstract measure spaces, providing a unified framework for probability theory, harmonic analysis, and functional analysis.

## The mathematical DNA of modern analysis

Lebesgue's theory became the mathematical DNA that runs through virtually all of modern analysis:

- **Functional Analysis** - $$L^p$$ spaces are defined using Lebesgue integration
- **Probability Theory** - probability measures are special cases of Lebesgue-type measures
- **Harmonic Analysis** - Fourier analysis relies fundamentally on Lebesgue integration
- **Partial Differential Equations** - weak solutions are defined using Lebesgue integrals
- **Stochastic Processes** - Martingale theory and stochastic integration build on measure theory

# Littlewood's Three Principles - The Philosophical Impact

[John Edensor Littlewood](https://en.wikipedia.org/wiki/John_Edensor_Littlewood) beautifully captured the philosophical implications of Lebesgue's theory in his "three principles," which reveal how measure theory aligns mathematical rigor with geometric intuition:

## Principle 1 - every measurable set is nearly a finite union of intervals

Any measurable set $$E$$ can be approximated arbitrarily well by finite unions of intervals.

$$\forall \epsilon > 0, \exists \text{ intervals } I_1, \ldots, I_n : \mu\left(E \triangle \bigcup_{i=1}^n I_i\right) < \epsilon$$

## Principle 2 - every measurable function is nearly continuous (Lusin's Theorem)

For any measurable function $$f$$ on $$[a,b]$$ and $$\epsilon > 0$$, there exists a continuous function $$g$$ such that:

$$\mu\{x : f(x) \neq g(x)\} < \epsilon$$

## Principle 3 - every convergent sequence is nearly uniformly convergent (Egorov's theorem)

If $$f_n \to f$$ almost everywhere on a set of finite measure, then for any $$\epsilon > 0$$, there exists a set $$A$$ with $$\mu(A) < \epsilon$$ such that $$f_n \to f$$ uniformly on the complement of $$A$$.

These principles reveal that Lebesgue's theory doesn't abandon classical analysis—it shows that measurable objects are always *close* to the well-behaved objects of classical analysis.

# Broader Mathematical Impacts

## Immediate consequences

Lebesgue's theory immediately resolved numerous problems that had puzzled 19th-century analysts:

<h3>Term-by-term integration</h3>
When can we integrate an infinite series term by term? The dominated convergence theorem provides a definitive answer.

<h3>Differentiation of Integrals</h3>
[The Fundamental Theorem of Calculus](https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus) extends beautifully to the Lebesgue setting, revealing deep connections between differentiation and integration.

<h3>Function spaces</h3>

The $$L^p$$
spaces $$L^p(\mu) = \{f : \int |f|^p \, d\mu < \infty\}$$
become natural objects of study, leading to the development of functional analysis.

## Revolutionary applications

<h3>Probability theory</h3>

Lebesgue's theory provided the rigorous foundation for modern probability theory. Random variables became measurable functions, and expectation became Lebesgue integration with respect to probability measures.

<h3>Harmonic analysis</h3>

Fourier analysis was transformed by Lebesgue integration.
The $$L^2$$ theory of Fourier series,
[Plancherel's theorem](https://en.wikipedia.org/wiki/Plancherel_theorem),
and the development of abstract harmonic analysis all depend fundamentally on Lebesgue's insights.

<h3>Functional analysis</h3>

The theory of Banach and Hilbert spaces, operator theory, and the spectral theorem all emerged from the function space perspective enabled by Lebesgue integration.

# A Personal Reflection on Mathematical Beauty

When I first encountered measure theory, I was struck by something profound
&ndash;
here was a theory that resolved a seemingly technical problem (extending the Riemann integral) but in doing so revealed fundamental principles about the nature of mathematical structure itself.

The beauty of measure theory lies in how it transforms seemingly complex problems into natural consequences of a few elegant principles. The characteristic function of rationals, which seems pathological from a Riemann perspective, becomes perfectly natural in the Lebesgue framework—its integral is exactly what our intuition suggests it should be.

## The universality of Lebesgue's vision

What moves me most about Lebesgue's achievement is its universality.
Unlike some mathematical theories that solve specific problems,
measure theory reveals structural principles that apply across mathematics.

- The same measure-theoretic ideas that handle pathological functions on the real line
	also describe the geometry of infinite-dimensional spaces.
- The integration techniques that resolve convergence issues in analysis
	also provide the foundation for *probability theory* and *quantum mechanics*.
- The abstract measure spaces that generalize Lebesgue measure
	provide the setting for *modern algebraic topology* and *representation theory*.

This universality suggests that Lebesgue didn't just solve a technical problem—he glimpsed something fundamental about the mathematical structure of reality itself.

# Modern Developments and Continuing Impacts

## Measure theory today

Lebesgue's theory continues to evolve and find new applications.

<h3>Geometric measure theory</h3>

The study of measures on geometric objects (curves, surfaces &amp; fractals) extends Lebesgue's ideas to understand the *size* of irregular geometric objects.

<h3>Ergodic theory</h3>

The study of measure-preserving dynamical systems uses Lebesgue-type measures to understand long-term behavior of dynamical systems.

<h3>Stochastic analysis</h3>

Modern probability theory, including stochastic differential equations and mathematical finance, builds on sophisticated extensions of Lebesgue integration.

## Digital age

Even in our computational era, measure theory remains central.

<h3>Machine learning</h3>

The theoretical foundations of machine learning rely heavily on measure theory for understanding convergence of algorithms and generalization bounds.

<h3>Signal processing</h3>

Digital signal processing uses sophisticated measure-theoretic techniques for analyzing and processing signals.

<h3>Quantum computing</h3>

The mathematical foundations of quantum mechanics and quantum computing are built on measure theory and functional analysis.

# Lessons for Mathematical Thinking

<!--## What Lebesgue teaches us about mathematical progress-->

Lebesgue's achievement illustrates several profound lessons about mathematical thinking.

<h3>Question fundamental assumptions</h3>

Lebesgue succeeded by questioning the assumption that integration must proceed by partitioning the domain.
<span id="question-most-basic-assumptions">Sometimes the biggest breakthroughs come from examining our most basic assumptions.</span>

<h3>Seek the right abstractions</h3>

By focusing on the abstract notion of measure before constructing integration, Lebesgue found the right level of abstraction to solve the problem.
<span id="find-right-abstract">The power of mathematics often lies in finding the right abstract framework.</span>

<h3>Build on geometric intuition</h3>

Despite its abstract nature, measure theory is deeply rooted in geometric intuition about *size* and *area*. The most powerful abstract theories often preserve and refine our intuitive understanding.

<h3>Look for unifying principles</h3>

Lebesgue's theory succeeded because it found unifying principles
(measurability &amp; countable additivity) that made diverse phenomena coherent.
Mathematical beauty often emerges from unification.

# Conclusion - Continuing Revolution

More than a century after Lebesgue's breakthrough,
measure theory continues to be one of the most active and influential areas of mathematics.
Its principles shape our understanding of everything from the behavior of stock markets
to the structure of quantum systems.

But perhaps most importantly, Lebesgue's achievement demonstrates something profound about the nature of mathematical truth itself.
By seeking to understand the *right* notion of measure and integration,
Lebesgue uncovered principles that seem to reflect fundamental aspects of mathematical reality—principles that continue to illuminate new areas of mathematics and science.

<span id="highlight-conceptual-revolution">The creation of measure theory wasn't just a mathematical advancement—it was a conceptual revolution that fundamentally changed how we understand the very notion of *size* and *integration* in mathematics.
And in revealing these universal principles, Lebesgue showed us that the search for mathematical truth often leads to insights far deeper and more beautiful than we initially imagined.</span>

# Connection to the Universal Truth

As I reflect on Lebesgue's achievement in the context of my broader journey toward understanding the universal mathematical truth,
I'm struck by how measure theory exemplifies the patterns I've observed throughout mathematics:

- **universal principles** (measurability, countable additivity) that apply across diverse contexts
- **elegant abstraction** that reveals deeper structural truths
- **unification** of previously disparate phenomena under common principles
- **practical power** that emerges from theoretical understanding

These same patterns appear in my explorations of [inequalities](/math/inequalities), [abstract algebra](/math/abstract-algebra), and throughout the mathematical landscape. They suggest that mathematics isn't just a collection of techniques, but a coherent exploration of universal structural principles.

<span id="beautiful-examples">Lebesgue's measure theory stands as one of the most beautiful examples
of how the search for mathematical truth leads to insights that transform our understanding not just of specific problems,
but of the fundamental nature of mathematical reasoning itself.</span>

# Your Journey into Measure Theory

If you're encountering measure theory for the first time, I encourage you to appreciate both its technical power and its conceptual beauty. Start with the geometric intuition—understanding measure as a sophisticated notion of *size*—and gradually build toward the abstract theory.

Remember that every technical definition serves a conceptual purpose. The somewhat complex definition of measurability, for instance, ensures that our notion of measure behaves the way our geometric intuition suggests it should.

Most importantly, see measure theory as part of the broader mathematical quest to understand universal principles of structure and relationship. In mastering these concepts, you're not just learning techniques—you're participating in humanity's ongoing exploration of mathematical truth.

# Invitation to Continued Exploration

Measure theory opens doors to many of the most beautiful and powerful areas of modern mathematics. Whether your interests lie in probability theory, functional analysis, or differential equations, the principles you encounter here will provide the foundation for deeper understanding.

I invite you to explore these connections and to share your own insights and questions. The beauty of mathematics lies not just in individual understanding, but in the community of minds working together to uncover universal truths.

Please feel free to reach out to me at [sunghee.yun@gmail.com](mailto:sunghee.yun@gmail.com) with <span style="color: blue;">**"universal truth"**</span> in the subject line. Let's continue this exploration of mathematical beauty and truth together.

[Sunghee
<br>
<br>
Mathematician, Thinker, Finder, and Truth-Seeker
<br>
Entrepreneur, Engineer, Scientist, Business Developer, Creator, and Connector](/)

---

*This blog post explores another territory from my
[{{ math_landscape.title }}]({{ math_landscape.url }})
— a serendipitous creation that began as personal LaTeX slides and evolved
into a comprehensive exploration of mathematical beauty and universal truth.
Measure theory represents a foundational territory in this vast landscape,
connecting with inequalities, abstract algebra, convex optimization, and topology
in revealing the deeper structural principles that govern mathematical reasoning.*

<script>
// Function to get URL parameters
function getUrlParameter(name) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(name);
}

// Function to auto-play audio based on URL parameter
function autoPlayAudio() {
    const audioParam = getUrlParameter('audio');
    if (audioParam) {
        const audioElement = document.getElementById(audioParam);
        if (audioElement) {
            // Scroll to the audio element
            audioElement.scrollIntoView({ behavior: 'smooth', block: 'center' });

            // Add a small delay to ensure the page has loaded
            setTimeout(() => {
                audioElement.play().catch(error => {
                    console.log('Auto-play was prevented by browser:', error);
                    // Highlight the audio element if auto-play fails
                    audioElement.style.border = '3px solid #ff6b6b';
                    audioElement.style.borderRadius = '5px';
                });
            }, 500);
        }
    }
}

// Run the function when the page loads
document.addEventListener('DOMContentLoaded', autoPlayAudio);
</script>
