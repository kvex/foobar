%rebase base title=post.title, categories=categories, active_category=post.category

<div class="single">
	<h1>{{ post.title }}</h1>
	{{ post.content }}
	<div class="date">{{ post.pub_date }}</div>
</div>
