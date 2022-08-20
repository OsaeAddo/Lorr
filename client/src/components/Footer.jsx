import React from "react";
import { motion } from "framer-motion"


const Footer = () => {
    return (
        <footer className="grid gap-4 text-center pt-9 pb-4">
            <div className="grid gap-4 justify-center items-center">
                <section className="text-start">
                    <h2 className="font-bold text-2xl">Quicklinks</h2>
                    <ul>
                        <li>Category</li>
                        <li>Promo</li>
                        <li>Bridal Wear</li>
                        <li>Tops</li>
                    </ul>
                </section>
                <section className="text-start">
                    <h2 className="font-bold text-2xl">Services</h2>
                    <ul>
                        <li>Bridal Wear</li>
                        <li>Corsettes</li>
                        <li>Casual Wear</li>
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

            <div className="">
                <img src="" alt="L'orr-logo" />
            </div>
            <div className="">&copy; Copyright 2022</div>
        </footer>

    )
}

export default Footer;