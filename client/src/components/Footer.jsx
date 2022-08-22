import React from "react";
import { motion } from "framer-motion"


import logo from "../assets/logo/lorr-logo.jpeg"

const Footer = () => {
    return (
        <footer className="grid gap-4 text-center pt-9 pb-4 bg-gray-900 text-white">
            <div className="grid gap-4 justify-center items-center">
                <section className="text-start">
                    <h2 className="font-bold text-2xl">Quicklinks</h2>
                    <ul>
                        <li>Category</li>
                        <li>Promo</li>
                        <li>Bridal Wear</li>
                        <li>Evening Wear</li>
                    </ul>
                </section>
                <section className="text-start">
                    <h2 className="font-bold text-2xl">Services</h2>
                    <ul>
                        <li>Bridal Wear</li>
                        <li>Evening Wear</li>
                        <li>Casual</li>
                        <li>Corsettes</li>
                        <li>Tops</li>
                    </ul>
                </section>
                <section className="text-start">
                    <h2 className="font-bold text-2xl">Social Media</h2>
                    <ul>
                        <li>Facebook</li>
                        <li>Instagram</li>
                        <li>LinkedIn</li>
                        <li>Whatsapp</li>
                    </ul>
                </section>
                <section className="text-start">
                    <h2 className="font-bold text-2xl">About</h2>
                    <ul>
                        <li>Company</li>
                        <li>Developer</li>
                        <li>Documentation</li>
                        <li>Legal</li>
                    </ul>
                </section>
            </div>

            <div className="w-1/2 mx-auto">
                <img className="w-16" src={logo} alt="L'orr-logo" />
            </div>
            <div className="">&copy; Copyright 2022</div>
        </footer>

    )
}

export default Footer;