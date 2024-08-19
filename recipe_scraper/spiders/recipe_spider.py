import scrapy
from scrapy.spiders import SitemapSpider

class RecipeSpiderSpider(SitemapSpider):
    name = "recipe_spider"
    allowed_domains = ["recipe-free.com"]
    sitemap_urls = [
        "https://www.recipe-free.com/sitemap.xml",
        "https://www.recipe-free.com/sitemapindex.xml",
        "https://www.recipe-free.com/sitemap1.xml",
        "https://www.recipe-free.com/sitemap2.xml",
        "https://www.recipe-free.com/sitemap3.xml",
        "https://www.recipe-free.com/sitemap4.xml",
        "https://www.recipe-free.com/sitemap5.xml",
        "https://www.recipe-free.com/sitemaphttp.xml",
        "https://www.recipe-free.com/sitemapindexhttp.xml",
        "https://www.recipe-free.com/sitemap1http.xml",
        "https://www.recipe-free.com/sitemap2http.xml",
        "https://www.recipe-free.com/sitemap3http.xml",
        "https://www.recipe-free.com/sitemap4http.xml",
        "https://www.recipe-free.com/sitemap5http.xml"
    ]
    
    # Only filter recipe pages
    sitemap_rules = [
        (r"/recipes/", "parse_recipe")
    ]
    
    def parse_recipe(self, response):
        self.logger.info(f"Process url: {response.url}")
        
        uncleaned_prep_serving = response.css("div.times .times_tab .f12::text").getall()
        cleaned_prep_serving = [data.strip() for data in uncleaned_prep_serving if data.strip()]
        uncleaned_ingredients_instructions = response.css(".col-md-12 .for-padding-col p").getall()
        uncleaned_ingreients = uncleaned_ingredients_instructions[3]
        uncleaned_instructions = uncleaned_ingredients_instructions[4]
        cleaned_ingreidents = self.cleanResponse(uncleaned_ingreients)
        cleaned_instructions = self.cleanResponse(uncleaned_instructions)
        
        yield {
            'recipe_name': response.css("h1.red::text").get(),
            'recipe_author': response.css("a.fav::text").get(),        
            'link': response.url,
            'prep_time': cleaned_prep_serving[0],
            'serving_size': cleaned_prep_serving[1],
            'ingredients': cleaned_ingreidents,
            'insturctions': cleaned_instructions
        }
        
    def cleanResponse(self, response):
        shortenedResponse = response[30:-4]
        splitResponse = shortenedResponse.split("<br>")
        cleanedResponse = ""
        for segement in splitResponse:
            cleanedResponse += segement
        return cleanedResponse