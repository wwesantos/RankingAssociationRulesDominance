<h1>Ranking Association Rules by Dominance</h1>
Based on the article: <a href='http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=6495106'>Ranking and Selecting Association Rules Based on Dominance Relationship</a><br/>
Authors: S. Bouker ; LIMOS, Clermont Univ., Clermont-Ferrand, France ; R. Saidi ; S. B. Yahia ; E. M. Nguifo

<h1>Usage</h1>

<h2>Without optional parameters</h2>
<pre><code>
  		python .\main.py
</code></pre>

<h2>With all optional parameters</h2>
<ul>
  <li>-f -> input filename containing csv</li>
  <li>-a -> include all measures and rules in the rank file</li>
  <li>-o -> output filename</li>
</ul>
<pre><code>
  		python .\main.py -f .\data\RulesArticle.txt -a y -o .\output\RankedRules.txt
</code></pre>

<h2>Output</h2>
The output file will be .\output\RankedRules.txt


<h1>System Requirements</h1>
<p>You need <strong>Python &gt;= 3.5.0</strong>.</p>
