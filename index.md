


<center><p style="font-size:50px;">Analysis of  Amazon Review Data: Book vs eBook </p></center>

<center><img src="./imgs_charts/amazon_opening_logo.jpg" atl='amazon logo' height="400" width="600" alt="centered image"></center>

<!-- <p style="text-align:left; font-size:15px;">Github repo with full jupyter notebooks containing this analysis + data prep and PostgreSQL database creation available <a href="https://github.com/ukrainian-serge/amazon_product_reviews">HERE</a></p> -->

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ukrainian-serge/amazon_reviews.io/master)


<i>Sergey Kamilchu</i>  
Data source: [S3 amazon AWS review data set](https://s3.amazonaws.com/amazon-reviews-pds/tsv/index.txt)



<p style="text-align:left; font-size:20px;">Project Index</p>

*use these hyper links to jump to different sections*

<ol>
  <li style="text-align:left; font-size:15px;"><a href='#section1'>Why be interested in books?</a></li>
  <li style="text-align:left; font-size:15px;"><a href='#section2'>About the data</a></li>
  <li style="text-align:left; font-size:15px;"><a href='#section3'>Are paper books even relevant anymore?</a></li>
  <li style="text-align:left; font-size:15px;"><a href='#section4'>Analysis of paper vs digital title reviews</a></li>
  <li style="text-align:left; font-size:15px;"><a href='#section5'>Recommendation (END)</a></li>
</ol>

<a id="section1"></a>
<center><img src="./imgs_charts/in_the_dumps.jpg" atl='in the dumps' height="400" width="600" alt="centered image"/></center>

<center><p style="font-size:40px;">The greats read books</p></center>


<p style="text-align:left; font-size:30px;">Bill Gates</p>
<center><img src="./imgs_charts/bill_2.jfif" height="300" width="400"></center>
<p style="text-align:left">William Henry Gates III is an American business magnate, software developer, investor, and philanthropist. He is best known as the co-founder of Microsoft Corporation. During his career at Microsoft, Gates held the positions of chairman, chief executive officer, president and chief software architect, while also being the largest individual shareholder until May 2014</p>

*"Whether I'm at the office, at home, or on the road, I always have a stack of books I'm looking forward to reading." **~ Bill Gates***

<ul>
  <li style="text-align:left; font-size:15px;">reads about<a href="https://www.businessinsider.com/rich-people-like-to-read-2015-8"> 50 books per year</a></li>
  <li style="text-align:left; font-size:15px;">Bill wants you to read<a href='https://www.businessinsider.com/books-elon-musk-thinks-everyone-should-read-2018-4'>these 5 books from 2019 </a></li>
</ul>

<p style="text-align:left; font-size:30px;">Elon Musk</p>
<center><img src="./imgs_charts/elon_2.jfif" style="float: center" height="300" width="400"></center>
<p style="text-align:left">Elon Reeve Musk is an engineer and technology entrepreneur. He holds South African, Canadian, and U.S. citizenship and is the founder, CEO, and chief engineer/designer of SpaceX; CEO and product architect of Tesla, Inc.; founder of The Boring Company; co-founder of Neuralink; and co-founder and initial co-chairman of OpenAI</p>

*"The heroes of the books I read ... always felt a duty to save the world,"  **~ Elon Musk***

<ul>
  <li style="text-align:left; font-size:15px;"><a href='https://www.businessinsider.com/elon-musk-favorite-books-2014-10?op=1'> List </a>of his favorite books</li>
  <li style="text-align:left; font-size:15px;"><a href='https://www.businessinsider.com/books-elon-musk-thinks-everyone-should-read-2018-4'>List </a>of 12 books that shaped Elon</li>
</ul>

<p style="text-align:left; font-size:30px;">Oprah Winfrey</p>
<center><img src="./imgs_charts/oprah.jfif" style="float: center" height="300" width="400"></center>
<p style="text-align:left">Oprah Gail Winfrey is an American media executive, actress, talk show host, television producer, and philanthropist. She is best known for her talk show, The Oprah Winfrey Show, broadcast from Chicago, which was the highest-rated television program of its kind in history and ran in national syndication for 25 years from 1986 to 2011</p>

*"Reading gave me the power to see possibilities beyond what was allowed at the time." **~ Oprah Gail Winfrey***  



<p style="text-align:left; font-size:30px;">Larry Page</p>
<center><img src="./imgs_charts/larry_page.jpg" style="float: center" height="300" width="400"></center>
<p style="text-align:left;">Lawrence Edward Page is an American computer scientist and Internet entrepreneur. He is best known for being one of the co-founders of Google along with Sergey Brin. Page was the chief executive officer of Alphabet Inc. until stepping down on December 3, 2019</p>

*‘It’s not necessary to go to school to launch a business. I read a whole shelf of business books and that was basically all I needed’. **~ Larry Page***  


- [Books list](http://www.favobooks.com/enterpreneurs/110-Larry-Page-books-that-stimulate-your-mind.html) he was influenced by


<p style="font-size:30px;">Looks ok so far.. what about some science?</p>

<p>A very small list of studies showing the measurable positive changes that reading has on the most important asset we posses in our lifetime: the brain.</p>

<ul>
  <li style="text-align:left; font-size:15px;"><a href="https://srcd.onlinelibrary.wiley.com/doi/full/10.1111/cdev.12272"> Increase intelligence</a></li>
  <li style="text-align:left; font-size:15px;"><a href="https://n.neurology.org/content/81/4/314">It slows mental decline with age</a></li>
  <li style="text-align:left; font-size:15px;"><a href="https://science.sciencemag.org/content/342/6156/377.abstract">Can make you more empathetic</a></li>
</ul>

<hr>

<center><img src="./imgs_charts/book.jpg" height="400" width="600"></center>


<center><p style="font-size:50px;">Book or eBook?</p></center>

<p>Welcome to the analysis section. Here you will look into the <a href="https://authorsmstevens.com/2019/06/26/the-ebook-vs-printed-book-debate/">book vs ebook</a> debate. I want to investigate what the data contained within the reviews can tell us.</p>

<a id="section2"></a>

<center><p style="font-size:40px;">About the data</p></center>

<ul>

  <li style="font-size:15px;"><b>review_id</b></li>
  <ul>
    <li style="font-size:15px;">unique identifier for each row(observation) </li>
  </ul>

  <li style="font-size:15px;"><b>customer_id</b></li>

  <li style="font-size:15px;"><b>product_id</b>, eg.,</li>
  <ul>
    <li style="font-size:15px;">The Gulag Archipelago on <b>paper</b></li>
      <ul>
        <li style="font-size:15px;"><b>product_id:</b> A001 paper back</li>
        <li style="font-size:15px;"><b>product_id:</b> A002 hard cover</li>
        <li><b>...</b></li>
      </ul>
  
  <li style="font-size:15px;">The Gulag Archipelago on <b>digital</b></li>
    <ul>
      <li style="font-size:15px;"><b>product_id:</b> B001 kindle</li>
      <li style="font-size:15px;"><b>product_id:</b> B002 audio book</li>
      <li ><b>...</b></li>
    </ul>
  </ul>

  

  <li style="font-size:15px;"><b>product_title</b></li>

  <li style="font-size:15px;"><a href="https://www.businessinsider.com/how-amazon-review-stars-are-calculated-2019-6"><b>star_rating</b></a></li>
  <li style="font-size:15px;"><a href="https://www.businessinsider.com/how-amazon-review-stars-are-calculated-2019-6"><b>verified_purchase</b></a></li>
  <li style="font-size:15px;"><a href="https://www.amazon.com/gp/customer-reviews/top-reviewer-faq.html"><b>helpful_votes</b></a></li>
  <li style="font-size:15px;"><b>total_votes</b></li>
  <li style="font-size:15px;"><a href="https://www.amazon.com/gp/vine/help"><b>vine</b></a></li>
  <li style="font-size:15px;"><b>review_date</b></li>

</ul>    


<center><img src="./imgs_charts/kindle.jpg" atl='book' height="300" width="500"/></center>

<center><p style="text-align:center; font-size:40px;">Is paper in danger?</p></center>

<p style="text-align:left; font-size:15px;">Did introduction of digital ebooks produce decline in verified purchases of paper books?</p>
<a id="section3"></a>
<p style="text-align:left; font-size:20px;">Verified purchase reviews distributions chart</p>

<center><iframe src="./imgs_charts/1_verified_purchase_reviews.html"
    sandbox="allow-same-origin allow-scripts"
    width="625"
    height="625"
    scrolling="no"
    seamless="seamless"
    frameborder="">
</iframe></center>


*For above charts, a random fractional sample of each format was taken(0.01) because of the size of the data set*  
**Observations:**  


- `Digital` has larger sample size and went into full swing on amazon market starting 2014. Despite this, `Paper` reviews seem to be going steady and not declining in frequency.

---

<p style="text-align:left; font-size:15px;"><b>NOTE:</b> Every chart from here on, use chart right-side toolbar to:</p>
<ul style="text-align:left; font-size:15px;">
  <li style="text-align:left;"><b>PAN</b></li>
  <li style="text-align:left;"><b>WHEEL/BOX ZOOM</b></li>
  <li style="text-align:left;"><b>HOVER</b> cursor for inspection of data points</li>
  <li style="text-align:left;"><b>RESET</b> to re-align</li>
</ul>

---

<p style="text-align:left; font-size:20px;">Rolling average star rating Books vs eBooks</p>


<center><iframe src="./imgs_charts/2_month_rolling_avg_star_ratings.html"
    sandbox="allow-same-origin allow-scripts"
    width="720"
    height="520"
    scrolling="no"
    seamless="seamless"
    frameborder="">
</iframe></center>

**Observations:**

- It took `Digital` from 2007 - 2012 to stabilize its rolling averages on Amazon Market
- 2011 - 2012 both formats took a dip
- Rolling average of `Paper` OUTPERFORMS `Digital` format starting 2014 - onward  


<center><img src="./imgs_charts/books_1.jpg" atl='book' height="400" width="600"/></center>

<center><p style="font-size:40px;">Analysis of Paper vs Digital Titles</p></center>



<p style="text-align:left; font-size:20px;">Top titles sorted by <b>star rating</b> with stacked <b>helpful review</b> counts for comparison</p>

<a id="section4"></a>

<center><iframe src="./imgs_charts/3_helpful_votes_by_stars_both.html"
    sandbox="allow-same-origin allow-scripts"
    width="650"
    height="650"
    scrolling="no"
    seamless="seamless"
    frameborder="">
</iframe></center>

**Observation:**

- Above charts top(`Paper`) and bottom(`Digital`) titles are sorted by their respective `star_rating`
  - In all but three cases, `"Fearless", "Words of Radiance", "Being Mortal"`, `Paper` takes the cake in terms of helpful reviews written
  
*NOTE FROM ANALYST: `Words of Radiance` is one book of an excellent fantasy series!*

<p style="text-align:left; font-size:20px;">Top titles sorted by <b>verified purchase</b> counts with stacked <b>helpful review</b> counts for comparison</p>

<center><iframe src="./imgs_charts/4_helpful_votes_by_verified_both.html"
    sandbox="allow-same-origin allow-scripts"
    width="650"
    height="650"
    scrolling="no"
    seamless="seamless"
    frameborder="">
</iframe></center>

**Observation:**

- Above charts top(`Paper`) and bottom(`Digital`) titles are sorted by their respective `verified_purchase` sums
  - In all but one case, `The Fault In Our Stars`, `Paper` has higher `verified_purchase` `helpful_review` counts


<a id="section5"></a>

<center><img src="./imgs_charts/book_vs_ebook.jpg" atl='book' height="400" width="600"/></center>

<p style="text-align:left; font-size:50px;">Recommendations</p>

According to this simple analysis, `Paper` takes the cake, at least in terms of review quality. My recommendation? Buy whatever you want, but read the `Paper` reviews as they seem to be very helpful according to hundreds of thousands of review-readers.
More reading in general is a great idea, so I am not partial to either substrate. Also, cost wasn't taken into consideration during this analysis and that can play a large role in decision making of purchases.

Thanks for reading!
