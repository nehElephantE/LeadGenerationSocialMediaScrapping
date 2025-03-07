import React from 'react';
import Header from "../Header/Header";
import './About.css';

const About = () => {
    return (
        <>
            <Header/>

            <div className="w-screen">
                <div className="flex-col m-5">
                    <div className="flex justify-around items-center">
                        <div className="w-[50%] about-text">
                            <span className="about-heading block">About Us</span>
                            Our web application gives users the chance to join a community that uses customer collaboration to promote brands,
                            suggest products, and offer a forum for direct dialogue between influencers and interested parties. The interested parties can take advantage of a variety of benefits, including speaking with existing customers or influencers,
                            learning in-depth about the product of interest, getting any queries resolved, and receiving the best quote on any insurance
                            Bajaj Allianz offers in all markets.</div>
                        <div><img src={require("../Assets/about-image-1.png")}/></div>
                    </div>
                    <div className="flex justify-around items-center">
                        <div><img className="w-[50%]" src={require("../Assets/about-image-2.png")}/></div>
                        <div className="w-[80%] pr-10 about-text text-right">
                            Existing customers have the opportunity to become influencers on our website.
                            We have a special influencer programme that is essentially an incentive-based points-reward system,
                            wherein the influencer will receive a certain number of points for each interested party
                            that they convert into a customer as well as for performing product digital marketing activities, among other things.
                            These points will qualify you for incentives like cash, Amazon gift cards, and other goods.</div>
                    </div>
                </div>
            </div>

        </>
    );
};

export default About;