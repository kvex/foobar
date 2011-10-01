%rebase base title=category.name, categories=categories, active_category=category

<h1>{{ category.name }}</h1>

<div class="post-list">
%for post in paginator.object_list():
	<div class="post">
		<h2>{{ post.title }}</h2>
		<div class="date">{{ post.pub_date.strftime("%d.%m.%Y %H:%M") }}</div>
		<div class="category">Категория: <a href="{{ post.category.get_absolute_url }}">{{ post.category.name }}</a></div>
		<p>{{ post.teaser }}</p>
		<a href="{{ post.get_absolute_url }}">Читать полностью</a>
	</div>
%end
</div>

%for page in paginator.page_list():
	<a href="?page={{ page }}">{{ page }}</a>
%end
