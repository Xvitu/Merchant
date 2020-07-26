from merchant.src.domain.entities.product import Product


class ProductsFactory:

    @staticmethod
    def from_result_search(result_search):
        products = []
        for result_item in result_search.items:
            for result_product in result_item.pagemap.product:
                products.append(Product(result_product.name, result_product.url, result_product.image))

        return products
