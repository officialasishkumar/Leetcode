<h2><a href="https://leetcode.com/problems/create-target-array-in-the-given-order/description/">1389. Create Target Array in the Given Order</a></h2><h3>Easy</h3><hr><div>

<p>Given two arrays of integers <code>num</code>  and <code>index</code> . Your task is to create target array under the following rules:
<ul>
<li>Initially target array is empty.</li>
<li>From left to right read nums[i] and index[i], insert at index <code>index[i]</code> the value <code>nums[i]</code> in target array.</li>
<li>Repeat the previous step until there are no elements to read in <code>nums</code> and <code>index</code>.</li>
<li>Return the <em>target<em> array.</li>

It is guaranteed that the insertion operations will be valid.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [0,1,2,3,4], index = [0,1,2,2,1]
<strong>Output:</strong> [0,4,1,3,2]

<strong>Explanation:</strong>
<p>
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]
</p>
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3,4,0], index = [0,1,2,3,0]
<strong>Output:</strong> [0,1,2,3,4]

<strong>Explanation:</strong>
<p>
nums       index     target
1            0        [1]
2            1        [1,2]
3            2        [1,2,3]
4            3        [1,2,3,4]
0            0        [0,1,2,3,4]

</p>
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [1], index = [0]
<strong>Output:</strong> [1]

</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length,index.length &lt;= 100</code></li>
  <li><code>nums.length==index.length</sup></code></li>
  <li><code>0 &lt;= nums[i] &lt;= 100</code></li>
  <li><code>0 &lt;= index[i] &lt;= i</code></li>
</ul>
</div>
