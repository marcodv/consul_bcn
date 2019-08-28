package com.reljicd.service.impl;

import java.util.List;

import com.reljicd.model.Product;
import com.reljicd.repository.ProductRepository;
import com.reljicd.service.ShopCartService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class ShopCartServiceImpl implements ShopCartService {

    @Autowired
	private ProductRepository productRepository;

	@Override
	public List<Product> getAllProducts() {
		return this.productRepository.findAll();
	}

}