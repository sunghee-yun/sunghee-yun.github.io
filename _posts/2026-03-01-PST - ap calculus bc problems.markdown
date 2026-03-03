---
date: Mon Mar  2 23:13:06 PST 2026
last_modified_at: Mon Mar  2 23:13:06 PST 2026
title: "AP Calculus BC Problems"
permalink: /math/ap/calculus/bc
categories:
 - blog
 - Math
tags:
 - math
 - calculus
toc: true
toc_label: "&nbsp;Table of Contents"
toc_icon: "fa-solid fa-list"
toc_sticky: true
usemathjax: true
---

posted: {{ page.date| date: "%d-%b-%Y" }}
&
updated: {{ page.last_modified_at| date: "%d-%b-%Y" }}
{: .notice--primary}

**Share this on**
[LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url={{ site.url }}{{ site.baseurl }}{{ page.url }})
| [Instagram](https://www.instagram.com/)
| [Twitter (X)](https://x.com/intent/tweet?text={{ site.url }}{{ site.baseurl }}{{ page.url }})
| [Facebook](https://www.facebook.com/sharer/sharer.php?u={{ site.url }}{{ site.baseurl }}{{ page.url }})

# Unit 6

<ul>
<li>
Given the logistic differential equation $\dfrac{dA}{dt} = A\left(20-\dfrac{A}{4}\right)$
where $A(0) = 15$, what is $\lim_{t\to\infty} A(t)$?

<p>
Solution:

$$
\begin{eqnarray*}
\frac{dA}{A(20-A/4)} = dt
&\Longleftrightarrow&
\left( \frac{1}{A} + \frac{1}{80-A} \right) dA = 20dt
\\
&\Longleftrightarrow&
\log A - \log (80 - A) = 20 t + C
\\
&\Longleftrightarrow&
\log \left( \frac{A}{80 - A} \right) = 20 t + C
\\
&\Longleftrightarrow&
\log \left( \frac{1}{80/A - 1} \right) = 20 t + C
\\
&\Longleftrightarrow&
\log ( 80/A - 1 ) = -20 t - C
\\
&\Longleftrightarrow&
80/A = e^{-20 t - C} + 1
\\
&\Longleftrightarrow&
A = \frac{80}{e^{-20 t - C} + 1}
\end{eqnarray*}
$$


</p>

</li>
</ul>

