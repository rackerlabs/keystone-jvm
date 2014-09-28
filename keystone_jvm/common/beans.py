from org.openstack import Keystone
from org.openstack import TokenRepository
from org.springframework.boot import SpringApplication

context = SpringApplication.run(Keystone)
token = context.getBean(TokenRepository)
