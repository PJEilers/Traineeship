package com.example.Fullstack;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class AddressService {
    
    @Autowired
    private IAddressRepository repository;

    public List<Address> findAllAddresses () {
        List<Address> addresses = repository.findAll();

        return addresses;
    }

    public Address makeAddress(Address address) {
        return repository.save(address);
    }

    

}