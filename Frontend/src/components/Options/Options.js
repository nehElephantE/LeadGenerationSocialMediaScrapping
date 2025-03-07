import React from 'react';
import Header from "../Header/Header";
import Card from "../UI/Card/Card";
import './Options.css';
import Button from "../UI/Button/Button";
import {CheckIcon, TicketIcon} from "@heroicons/react/outline";
import { Link } from 'react-router-dom';

const Options = () => {
    return (
        <>
            <Header/>
            <div className="flex justify-around options-main mt-12">
                <div className="op-1">
                    <Link to="/verify">
                        <Card className="w-[80vh] py-10 px-[15%] text-center hover:bg-sky-200">
                        <span className="block text-left options-text">
                            Become an existing customer/influencer
                        </span>
                            <hr className="my-3 w-[25%] border-2 border-black"/>
                            <p className="text-left font-[Montserrat] font-[300] text-[20px]">
                                <ul>
                                    <li><CheckIcon className="h-8 mx-3 inline"/>Verify yourself as an existing customer of any insurance category</li>
                                    <li><CheckIcon className="h-8 mx-3 inline"/>Contribute to our webapp by converting leads to customers , collaborate with leads , boost brand performance</li>
                                    <li><CheckIcon className="h-8 mx-3 inline"/>Stand a chance to win exciting prizes (unlike zbc) , amazon gift codes and bajaj finserv goodies.</li>
                                </ul>
                            </p>
                        </Card>
                    </Link>
                </div>
                <div className="op-2">
                    <Link to="/community">
                        <Card className="w-[80vh] py-10 px-[15%] text-center hover:bg-sky-200">
                        <span className="block text-left options-text">
                            Browse other Bajaj products
                        </span>
                            <hr className="my-3 w-[25%] border-2 border-black"/>
                            <p className="text-left font-[Montserrat] font-[300] text-[20px]">
                                <ul>
                                    <li><CheckIcon className="h-8 mx-3 inline"/>Browse through the exciting range of products offered by Bajaj Finserv and stand a chance to avail special discounts available only here</li>
                                </ul>
                            </p>
                        </Card>
                    </Link>
                </div>
            </div>
        </>
    );
};

export default Options;