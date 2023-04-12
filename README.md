# data_camp-project_with_python


## "What did we learn from this project?"
- Trước hết, ta sẽ cần tải dữ liệu của bạn bè vào một dictionary. Điều này giúp tổ chức dữ liệu một cách dễ dàng hơn để xử lý và phân tích.
- Sau khi tải dữ liệu vào dictionary, bạn cần chuyển đổi nó thành một DataFrame. DataFrame, là một cấu trúc dữ liệu của thư viện Pandas trong Python, giúp bạn thực hiện nhiều thao tác phân tích dữ liệu một cách hiệu quả.
- Trước khi bắt đầu phân tích dữ liệu, bạn nên kiểm tra dữ liệu của mình bằng cách trực quan hóa nó. Điều này giúp bạn hiểu rõ hơn về cấu trúc và tính chất của dữ liệu.
- Sau khi kiểm tra dữ liệu ban đầu, bạn sẽ cần tải thêm dữ liệu từ một tệp CSV khác để thực hiện phân tích chi tiết hơn.
- Sau khi tải thêm dữ liệu, bạn sẽ cần lọc các bộ phim để tập trung vào phân tích của mình. Bước tiếp theo là tạo một biểu đồ phân tán để thể hiện mối quan hệ giữa các thuộc tính của các bộ phim.
- Sau khi tạo ra biểu đồ phân tán, bạn sẽ cần đi sâu hơn vào phân tích để hiểu rõ hơn về các mối quan hệ này. Bạn sẽ cần đánh dấu các bộ phim không phải là phim chính để loại bỏ chúng khỏi phân tích.
- Cuối cùng, bạn sẽ cần trực quan hóa dữ liệu của mình bằng cách sử dụng màu sắc để thể hiện các mối quan hệ giữa các thuộc tính khác nhau của các bộ phim.

## 1. Loading your friend's data into a dictionary
<p>If we're going to be working with this data, we know a good place to start would be to probably start working with <code>pandas</code>. But first we'll need to create a DataFrame from scratch.</p>

## 2. Creating a DataFrame from a dictionary
<p>To convert our dictionary <code>movie_dict</code> to a <code>pandas</code> DataFrame, we will first need to import the library under its usual alias. We'll also want to inspect our DataFrame to ensure it was created correctly. Let's perform these steps now.</p>

## 3. A visual inspection of our data
<p>Alright, we now have a <code>pandas</code> DataFrame, the most common way to work with tabular data in Python. Now back to the task at hand. We want to follow up on our friend's assertion that movie lengths have been decreasing over time. A great place to start will be a visualization of the data.</p>
<p>Given that the data is continuous, a line plot would be a good choice, with the dates represented along the x-axis and the average length in minutes along the y-axis. This will allow us to easily spot any trends in movie durations. There are many ways to visualize data in Python, but <code>matploblib.pyplot</code> is one of the most common packages to do so.</p>

## 4. Loading the rest of the data from a CSV
<p>Upon asking our friend for the original CSV they used to perform their analyses, they gladly oblige and send it. We now have access to the CSV file, available at the path <code>"datasets/netflix_data.csv"</code>. Let's create another DataFrame, this time with all of the data. Given the length of our friend's data, printing the whole DataFrame is probably not a good idea, so we will inspect it by printing only the first five rows.</p>

## 5. Filtering for movies!
<p>Fortunately, a DataFrame allows us to filter data quickly, and we can select rows where <code>type</code> is <code>Movie</code>. While we're at it, we don't need information from all of the columns, so let's create a new DataFrame <code>netflix_movies</code> containing only <code>title</code>, <code>country</code>, <code>genre</code>, <code>release_year</code>, and <code>duration</code>.</p>

## 6. Creating a scatter plot
<p>Okay, now we're getting somewhere. We've read in the raw data, selected rows of movies, and have limited our DataFrame to our columns of interest. Let's try visualizing the data again to inspect the data over a longer range of time.</p>
<p>This time, we are no longer working with aggregates but instead with individual movies. A line plot is no longer a good choice for our data, so let's try a scatter plot instead. We will again plot the year of release on the x-axis and the movie duration on the y-axis.</p>

## 7. Digging deeper
<p>Upon further inspection, something else is going on. Some of these films are under an hour long! Let's filter our DataFrame for movies with a <code>duration</code> under 60 minutes and look at the genres. This might give us some insight into what is dragging down the average.</p>

## 8. Marking non-feature films
<p>We could eliminate these rows from our DataFrame and plot the values again. But another interesting way to explore the effect of these genres on our data would be to plot them, but mark them with a different color.</p>

## 9. Plotting with color!
<p>This time, we'll also spruce up our plot with some additional axis labels and a new theme with <code>plt.style.use()</code>. The latter isn't taught in Intermediate Python, but can be a fun way to add some visual flair to a basic <code>matplotlib</code> plot.</p>

## 10. What next?
<p>Well, as we suspected, non-typical genres such as children's movies and documentaries are all clustered around the bottom half of the plot. But we can't know for certain until we perform additional analyses. </p>




