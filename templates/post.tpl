%rebase base title=post.title, categories=categories, active_category=post.category

<div class="single">
	<h1>{{ post.title }}</h1>
	<div class="date">{{ post.pub_date.strftime("%d.%m.%Y %H:%M") }}</div>
	<div class="category">Категория: <a href="{{ post.category.get_absolute_url }}">{{ post.category.name }}</a></div>
    <div class="content">
    	{{ post.content }}
    </div>
</div>
