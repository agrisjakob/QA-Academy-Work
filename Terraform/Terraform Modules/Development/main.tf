resource "azurerm_virtual_network" "example" {
  name                = "paris-net"
  resource_group_name = var.group
  location            = var.location
  address_space       = ["10.0.0.0/16"]
}

resource "azurerm_subnet" "internal" {
  name                 = "internal"
  resource_group_name  = var.group
  virtual_network_name = azurerm_virtual_network.example.name
  address_prefix       = "10.0.2.0/24"
}

resource "azurerm_linux_virtual_machine_scale_set" "example" {

  name                = "paris-scale-set"
  resource_group_name = var.group
  location            = var.location
  sku                 = "Standard_F2"
  instances           = 1
  admin_username      = "adminuser"
  zones               = ["1",]
  

  admin_ssh_key {
    username   = "adminuser"
    public_key = file("~/.ssh/id_rsa.pub")
  }
  lifecycle {
  ignore_changes      = [instances,]
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }

  os_disk {
    storage_account_type = "Standard_LRS"
    caching              = "ReadWrite"
  }

  network_interface {
    name    = "example"
    primary = true

    ip_configuration {
      name      = "internal"
      primary   = true
      subnet_id = azurerm_subnet.internal.id
    }
  }
}

resource "azurerm_monitor_autoscale_setting" "upscale" {
  name                = "upscale-paris"
  resource_group_name = var.group
  location            = var.location
  target_resource_id  = azurerm_linux_virtual_machine_scale_set.example.id

  profile {
    name = "launch"

    capacity {
      default = 3
      minimum = 3
      maximum = 3
      }
    recurrence {
      timezone  = "UTC"
      days      = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
      hours     = [10]
      minutes   = [0]
      }
    }
  profile {
    name = "take-down"
 
    capacity {
      default = 0
      minimum = 0
      maximum = 0
    }

    recurrence {
      timezone  = "UTC"
      days      = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
      hours     = [15]
      minutes   = [0]
    }
 } 
}
