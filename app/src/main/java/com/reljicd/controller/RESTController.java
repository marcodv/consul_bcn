package com.reljicd.controller;

import java.util.List;

import com.reljicd.model.Product;
import com.reljicd.service.ShopCartService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
@CrossOrigin
@RequestMapping(value = "/api")
public class RESTController {

    @Autowired
    private ShopCartService shopCartService;

    @RequestMapping(value = "/product", method = RequestMethod.GET)
    public ResponseEntity<List<Product>> getProductList() {
        List<Product> productList = this.shopCartService.getAllProducts();
        return new ResponseEntity<List<Product>>(productList,HttpStatus.OK);
    }

}