from .models import Box


def recommend_box(product):
    suitable_boxes = []

    for box in Box.objects.all():
        # Check weight
        if product.weight > box.max_weight:
            continue

        # Check dimensions.
        # Products can be rotated, so we compare all possible orientations.
        product_dimensions = [
            product.length,
            product.width,
            product.height,
        ]

        box_dimensions = [
            box.length,
            box.width,
            box.height,
        ]

        product_dimensions.sort()
        box_dimensions.sort()

        if all(
            product_dimension <= box_dimension
            for product_dimension, box_dimension
            in zip(product_dimensions, box_dimensions)
        ):
            suitable_boxes.append(box)

    if not suitable_boxes:
        return None

    return min(suitable_boxes, key=lambda box: box.cost)