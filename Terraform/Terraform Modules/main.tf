provider "azurerm" {
    features {}
}

resource "azurerm_resource_group" "example" {
    name = "terraform1"
    location = "West Europe"
}

module "paris" {
    source = "./Development"
    location = "West Europe"
    group = azurerm_resource_group.example.name
}

module "london" {
    source = "./Production"
    location = "uksouth"
    group = azurerm_resource_group.example.name
}

module "mumbai" {
    source = "./Staging"
    location = "uksouth"
    group = azurerm_resource_group.example.name
}