from django.contrib import admin

from .models import (
    Character,
    Comic,
    Fragment,
    Journey,
    Magazine,
    Person,
    Photo,
    Place,
    Route,
    Scene,
    Series,
    Step,
    Story,
    Tweet,
    Type_master,
    Venue,
    Web_comic,
)

# from django.contrib.gis.admin.options import GeoModelAdminMixin


class ComicInline(admin.TabularInline):
    model = Comic


class StoryWithWeb_comicInline(admin.TabularInline):
    model = Web_comic
    fk_name = "story"
    readonly_fields = [
        "display_story",
        "part_number",
        "pages",
        "title",
    ]
    exclude = [
        "cw_published",
        "cw_url",
        "nico_published",
        "nico_url",
        "memo",
    ]


class MagazineInline(admin.TabularInline):
    model = Magazine


class PlaceWithFragmentInline(admin.TabularInline):
    model = Fragment
    fk_name = "place"
    readonly_fields = ["character", "type_master", "title"]
    exclude = ["memo", "story", "web_comic", "url"]


class StoryWithFragmentInline(admin.TabularInline):
    model = Fragment
    fk_name = "story"
    exclude = ["memo", "web_comic", "character", "place", "url"]
    readonly_fields = ["title", "type_master"]


class StoryWithVenueInline(admin.TabularInline):
    model = Venue
    fk_name = "story"
    exclude = []
    readonly_fields = []


class Web_comicWithFragmentInline(admin.TabularInline):
    model = Fragment
    fk_name = "web_comic"


class JourneyInline(admin.TabularInline):
    model = Journey


class ComicWithStoryInline(admin.TabularInline):
    model = Story
    fk_name = "comic"
    fields = ["title", "subtitle", "type_master"]
    exclude = ["camera_center_place", "camera_zoom_level", "journey", "magazine"]


class JourneyWithStoryInline(admin.TabularInline):
    model = Story
    fk_name = "journey"
    fields = ["title", "subtitle", "type_master"]
    readonly_fields = ["title", "subtitle", "type_master"]
    extra = 0


class StoryWithRouteInline(admin.TabularInline):
    model = Route
    fk_name = "story"
    exclude = ["memo"]


class VenueInline(admin.TabularInline):
    model = Venue


class PlaceInline(admin.TabularInline):
    model = Place


class RouteWithStepInline(admin.TabularInline):
    model = Step
    fk_name = "route"
    extra = 20
    show_change_link = True


class PlaceWithStepInline(admin.TabularInline):
    model = Step
    fk_name = "place"
    extra = 20
    show_change_link = True


class PlaceWithSceneInline(admin.TabularInline):
    model = Scene
    fk_name = "place"
    exclude = ["memo"]
    readonly_fields = ["story", "character", "type_master", "page"]


class StoryWithSceneInline(admin.TabularInline):
    model = Scene
    fk_name = "story"
    exclude = ["memo"]
    readonly_fields = [
        "character",
        "place",
        "type_master",
    ]


class FragmentWithCharacterInline(admin.TabularInline):
    model = Character
    fk_name = "fragment"


class PersonWithTweetInline(admin.TabularInline):
    model = Tweet
    fk_name = "person"


class StepWithTweetInline(admin.TabularInline):
    model = Tweet
    fk_name = "step"


class PersonWithPhotoInline(admin.TabularInline):
    model = Photo
    fk_name = "person"


class StepWithPhotoInline(admin.StackedInline):
    model = Photo
    fk_name = "step"
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "type_master",
                    "title",
                    "username",
                    "person",
                )
            },
        ),
        (None, {"fields": ("get_photo",)}),
    )
    readonly_fields = ["type_master", "title", "username", "person", "get_photo"]
    exclude = ["link", "image_src", "width", "height"]
    extra = 0


class PersonInline(admin.TabularInline):
    model = Person


class TweetWigetInline(admin.StackedInline):
    model = Tweet
    fields = ["tweet_id", "get_widget"]
    readonly_fields = ["get_widget"]
    extra = 0


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    fields = [
        "short_title",
        "title",
        "author",
        "publisher",
        "label",
        "magazine_title",
        "site",
        "rel_series_id",
    ]
    list_display = (
        "id",
        "short_title",
        "title",
        "author",
        "publisher",
    )
    list_display_links = (
        "short_title",
        "title",
    )


@admin.register(Comic)
class ComicAdmin(admin.ModelAdmin):
    fields = [
        "series",
        "number",
        "title",
        "obi",
        "issued",
        "released",
        "cover_image",
        "isbn",
        "memo",
    ]
    list_filter = ["series"]
    inlines = [ComicWithStoryInline]
    search_fields = ["title", "obi"]
    list_display = (
        "series",
        "number",
        "title",
    )
    list_display_links = (
        "number",
        "title",
    )


@admin.register(Web_comic)
class Web_comicAdmin(admin.ModelAdmin):
    fields = [
        "title",
        "part_number",
        "pages",
        "cw_published",
        "cw_url",
        "nico_published",
        "nico_url",
        "story",
        "memo",
    ]
    # list_filter = ["type_master", ""]
    search_fields = ["title", "memo"]
    autocomplete_fields = ["story"]
    list_display = (
        "id",
        "story",
        "part_number",
        "title",
    )
    list_display_links = (
        "part_number",
        "title",
    )
    date_hierarchy = "cw_published"


@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    fields = ["title", "released", "cover_image", "site", "tag_line", "memo"]
    # list_filter = ["type_master", ""]
    search_fields = ["title", "tag_line", "memo"]
    list_display = (
        "id",
        "title",
        "released",
        "tag_line",
    )
    list_display_links = (
        "title",
        "released",
    )
    date_hierarchy = "released"


@admin.register(Type_master)
class Type_masterAdmin(admin.ModelAdmin):
    fields = ["name", "key", "value"]
    list_filter = ["key"]
    search_fields = ["name", "key", "value"]
    list_display = (
        "id",
        "key",
        "value",
        "name",
    )
    list_display_links = ("name",)


@admin.register(Fragment)
class FragmentAdmin(admin.ModelAdmin):
    fields = [
        "title",
        "url",
        "type_master",
        "place",
        "story",
        "web_comic",
        "character",
        "memo",
    ]
    # inlines = [FragmentWithCharacterInline]
    # list_filter = ["type_master", ""]
    search_fields = ["title", "memo"]
    autocomplete_fields = ["place", "story", "web_comic"]
    list_display = (
        "id",
        "title",
        "place",
        "type_master",
        "story",
        "web_comic",
    )
    list_display_links = ("title",)


@admin.register(Journey)
class JourneyAdmin(admin.ModelAdmin):
    fields = ["key", "number", "type_master", "memo"]
    inlines = [JourneyWithStoryInline]
    # list_filter = ["type_master", ""]
    search_fields = ["key", "number", "memo"]
    list_display = (
        "key",
        "journey_name",
        "type_master",
    )
    list_display_links = (
        "key",
        "journey_name",
    )


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    fields = [
        "title",
        "subtitle",
        "type_master",
        "journey",
        "comic",
        "magazine",
        "camera_center_place",
        "camera_zoom_level",
        "display_venues",
        "display_routes",
    ]
    inlines = [
        StoryWithWeb_comicInline,
        StoryWithSceneInline,
        StoryWithFragmentInline,
    ]
    list_filter = ["journey"]
    search_fields = ["title", "subtitle"]
    list_display = (
        "id",
        "journey",
        "title",
        "subtitle",
        "type_master",
    )
    list_display_links = (
        "subtitle",
        "title",
    )
    readonly_fields = ["display_venues", "display_routes"]


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    fields = ["name", "type_master", "story", "memo"]
    # list_filter = ["type_master", ""]
    search_fields = ["name", "memo"]
    inlines = [RouteWithStepInline]
    list_display = (
        "id",
        "name",
        "type_master",
    )
    list_display_links = (
        "id",
        "name",
    )


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    fields = ["name", "type_master", "story"]
    list_filter = ["type_master"]
    search_fields = ["name"]
    list_display = (
        "id",
        "name",
        "type_master",
    )
    list_display_links = ("name",)
    filter_horizontal = ["story"]


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "venue",
        "address",
        "latitude",
        "longitude",
        "altitude",
        "point_on_map",
        "memo",
    ]
    inlines = [PlaceWithFragmentInline, PlaceWithSceneInline, PlaceWithStepInline]
    list_filter = ["venue"]
    search_fields = ["name"]
    autocomplete_fields = ["venue"]
    list_display = (
        "id",
        "name",
        "latitude",
        "longitude",
        "altitude",
        "venue",
    )
    list_display_links = (
        "altitude",
        "latitude",
        "longitude",
        "name",
    )
    readonly_fields = ["point_on_map"]


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    class Media:
        js = ("https://platform.twitter.com/widgets.js",)

    fields = ["datetime", "number", "route", "place", "point_on_map"]
    inlines = [TweetWigetInline, StepWithPhotoInline]
    list_filter = ["route"]
    search_fields = ["datetime"]
    autocomplete_fields = ["route", "place"]
    list_display = (
        "route",
        "place",
        "number",
        "datetime",
    )
    list_display_links = (
        "datetime",
        "number",
        "place",
    )
    date_hierarchy = "datetime"
    readonly_fields = ["point_on_map"]


@admin.register(Scene)
class SceneAdmin(admin.ModelAdmin):
    fields = ["story", "place", "character", "page", "type_master", "memo"]
    list_filter = ["type_master", "story"]
    search_fields = ["memo"]
    autocomplete_fields = ["story", "place"]
    list_display = (
        "story",
        "place",
        "comic_number",
        "page",
        "type_master",
    )
    list_display_links = (
        "page",
        "place",
    )


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    fields = ["name", "description", "type_master"]
    # inlines = [FragmentInline]
    # list_filter = ["type_master", ""]
    search_fields = ["name", "description"]
    list_display = (
        "id",
        "name",
        "type_master",
    )
    list_display_links = ("name",)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    fields = [
        "title",
        "username",
        "image_src",
        "link",
        "type_master",
        "height",
        "width",
        "step",
        "person",
        "get_photo",
    ]
    # list_filter = ["type_master", ""]
    search_fields = ["username", "title"]
    autocomplete_fields = ["step", "person"]
    list_display = (
        "id",
        "title",
        "username",
        "step",
        "type_master",
        "person",
    )
    list_display_links = (
        "id",
        "title",
        "username",
    )
    readonly_fields = ["get_photo"]


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    class Media:
        js = ("https://platform.twitter.com/widgets.js",)

    fields = [
        "step",
        "type_master",
        "username",
        "person",
        "tweet_id",
        "url",
        "description",
        "get_widget",
    ]
    # list_filter = ["type_master", ""]
    search_fields = ["username", "description"]
    autocomplete_fields = ["step", "person"]
    list_display = (
        "id",
        "tweet_id",
        "username",
        "person",
        "step",
        "type_master",
    )
    list_display_links = (
        "id",
        "tweet_id",
        "username",
    )
    readonly_fields = ["get_widget"]


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fields = ["name", "type_master", "user", "memo"]
    # list_filter = ["type_master", ""]
    search_fields = ["name", "memo"]
    list_display = (
        "id",
        "name",
        "type_master",
        "user",
    )
    list_display_links = ("name",)
