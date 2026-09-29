from django.test import TestCase
from .models import Product, Box
from .services import recommend_box


class BoxRecommendationTest(TestCase):

    def test_recommends_cheapest_suitable_box(self):
        product = Product.objects.create(
            name="Laptop",
            length=30,
            width=20,
            height=5,
            weight=2
        )

        Box.objects.create(
            name="Large Box",
            length=40,
            width=30,
            height=10,
            max_weight=10,
            cost=100
        )

        Box.objects.create(
            name="Small Box",
            length=35,
            width=25,
            height=10,
            max_weight=5,
            cost=50
        )

        box = recommend_box(product)

        self.assertEqual(box.name, "Small Box")

    def test_rejects_box_when_weight_exceeds_capacity(self):
        product = Product.objects.create(
            name="Heavy Product",
            length=10,
            width=10,
            height=10,
            weight=10
        )

        Box.objects.create(
            name="Light Box",
            length=20,
            width=20,
            height=20,
            max_weight=5,
            cost=20
        )

        box = recommend_box(product)

        self.assertIsNone(box)

    def test_rejects_box_when_dimensions_do_not_fit(self):
        product = Product.objects.create(
            name="Large Product",
            length=50,
            width=50,
            height=50,
            weight=2
        )

        Box.objects.create(
            name="Small Box",
            length=20,
            width=20,
            height=20,
            max_weight=10,
            cost=20
        )

        box = recommend_box(product)

        self.assertIsNone(box)