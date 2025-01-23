<div>

    {% if config.site_name %}
        <h1>{{ config.site_name }}</h1>
    {% endif %}

    {% if config.extra.homepage %}
        by <h3><a href="{{ config.extra.homepage }}">{{ config.extra.homepage }}</a></h3>
    {% endif %}

</div>


<table>

    {% if config.site_description %}
    <tr>
        <td>Description</td>
        <td>{{ config.site_description }}</td>
    </tr>
    {% endif %}

    {% if config.site_url %}
    <tr>
        <td>Hosted at</td>
        <td>{{ config.site_url }}</td>
    </tr>
    {% endif %}

    {% if config.repo_url %}
    <tr>
        <td>Repository</td>
        <td><a href="{{ config.repo_url }}">{{ config.repo_url }}</a></td>
    </tr>
    {% endif %}

    {% if config.copyright %}
    <tr>
        <td>Copyright</td>
        <td>{{ config.copyright }}</td>
    </tr>
    {% endif %}

</table>
