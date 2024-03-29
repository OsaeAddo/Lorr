import React, { Component } from "react";

import axios from 'axios'


class Products extends Component {
    state = {
        products: []
    }
    
    // Ensure that Api call is made at correct time during 
    // the React lifecycle
    componentDidMount() {
      this.getProducts()
    }
    
    getProducts() {
        axios 
          .get('http://127.0.0.1:8000/api/v1.0/products')
          .then(res => {
            this.setState({ products: res.data })
          })
          .catch(err => {
            console.log(err)
          })
    }

    render() {
        return (
          <div>
            {this.state.products.map(
              item => (
                <div key={item.id}>
                  <h1 className="text-3xl font-bold underline">{item.item_name}</h1>
                  <p>{item.price}</p>
                  <p>{item.discount_price}</p>
                  <p>{item.category}</p>
                  <p>{item.label}</p>
                  <p>{item.description}</p>
                </div>
              )
            )}
          </div>
        )
      }
}


export default Products;