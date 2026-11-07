from fastmcp import FastMCP

mcp = FastMCP('Amazon Ecommerce')

# Tool-1
@mcp.tool
def search_products():
    """The available products in amazon"""
    products = ['Mobiles', 'Laptops', 'Headphones', 'SmartWatches', 'SmartBands']
    return products

# Tool-2
@mcp.tool
def get_offers():
    """This tool gives the offer details of the products"""
    offers = {'Mobiles' : '10%', 'Laptops' : '15%', 'Headphones' : '12%'}
    return offers

# Tool-3
@mcp.tool
def order_status():
    """The order status of the product to be delivered"""
    return "The product is delivered"

# Tool-4
@mcp.tool
def payment():
    """This tool tells whether the payment is done or not"""
    status = 'yes'
    return status


if __name__ == '__main__':
    mcp.run(transport = 'streamable-http', port = 50001, host = '0.0.0.0')
    