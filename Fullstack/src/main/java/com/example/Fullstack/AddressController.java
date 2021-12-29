package com.example.Fullstack;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import java.util.List;

@RestController
@CrossOrigin(maxAge=3600)
public class AddressController {

    @Autowired
    private AddressService service;

    @RequestMapping(value = "/addresses")
    public List<Address> find() {
        return service.findAllAddresses();
    }

    @RequestMapping(method = RequestMethod.POST, value = "/maakadresaan")
    public Address makeAddress (@RequestBody Address address) {
        return service.makeAddress(address);
    }


}
