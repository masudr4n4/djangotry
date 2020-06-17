from django.test import SimpleTestCase
from django.urls import reverse,resolve
from .views import HomePageView

# Create your tests here.
class HomePageTests(SimpleTestCase):
   #if i user setup method don't need to take response again and again 
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)
    
    def test_homepage_status_code(self):
       # response = self.client.get('/')
        self.assertEqual(self.response.status_code,200)
    def test_homepage_url_name(self):
       # response = self.client.get(reverse('home'))
        self.assertEqual(self.response.status_code,200)
    def test_homepage_template(self):
        #response = self.client.get('/')
        self.assertTemplateUsed(self.response,template_name='home.html')
    
    def test_homepage_cointains_correct_html(self):
        #response = self.client.get('/')
        self.assertContains(self.response,'Hompage For Book Store')
    
    def test_homepage_does_not_incorrect(self):
       # response = self.client.get('/')
        self.assertNotContains(self.response,'I am not hompage')
    
    def test_homepage_resolve_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,HomePageView.as_view().__name__
        )