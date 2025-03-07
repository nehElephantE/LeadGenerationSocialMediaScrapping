import React from 'react';
import Header from "../Header/Header";
import {Navigate} from "react-router-dom";
import Card from "../UI/Card/Card";
import Profile from "../Profile/Profile";
import Banner from "../UI/Banner/Banner";
import {PaperAirplaneIcon, PaperClipIcon, SearchIcon} from "@heroicons/react/outline";
import Chat from "../Chat/Chat";
import './Homepage.css';
import CommCard from "../UI/CommCard/CommCard";


const Homepage = () => {
    return (
        <>
            <Header/>
            <div className="home__section h-[91vh] overflow-hidden pt-3">

                {/*{!user && <Navigate replace to="/"/>}*/}
                {/*<div className="flex h-56 bg-[#000000] text-white">fnsjkfjksnjksff</div>*/}
                <div className="flex">
                    <div className="flex flex-col gap-5">
                        <Card className="card py-6 ml-5 w-[20rem]">

                    <span className="subheading px-6">
                        Chat
                    </span>
                            <hr/>
                            <div className="h-[20vh] flex-grow overflow-y-scroll">
                                <Profile type="square" name="dude 1"/>
                                <Profile type="square" name="dude 2"/>
                                <Profile type="square" name="dude 3"/>
                                <Profile type="square" name="dude 4"/>
                                <Profile type="square" name="dude 4"/>
                                <Profile type="square" name="dude 4"/>
                            </div>
                        </Card>

                        <Card className="card py-6 ml-5 w-[20rem]">
                    <span className="subheading px-6">
                        Circles
                    </span>
                            <hr/>
                            <div className="h-[42vh] flex-grow overflow-y-scroll">
                                <Profile type="rounded-full" name="Circle 1"/>
                                <Profile type="rounded-full" name="Circle 2"/>
                                <Profile type="rounded-full" name="Circle 3"/>
                                <Profile type="rounded-full" name="Circle 4"/>
                                <Profile type="rounded-full" name="Circle 5"/>
                                <Profile type="rounded-full" name="Circle 6"/>
                                <Profile type="rounded-full" name="Circle 7"/>
                                <Profile type="rounded-full" name="Circle 7"/>
                                <Profile type="rounded-full" name="Circle 7"/>
                                <Profile type="rounded-full" name="Circle 7"/>
                            </div>

                            {/*for displaying through firebase*/}
                            {/*{channels?.docs.map((doc)=>(*/}
                            {/*    <Channel key={doc.id} id={doc.id} channelName={}/>*/}
                            {/*))}*/}

                        </Card>
                    </div>

                    <div className="flex flex-col w-full mx-5 mt-2">
                        <div className="home__banner h-[30%] flex flex-col">
                            <div className="home__banner-text text-center">
                                <h1 className="text-center">Find your Circle!</h1>
                            </div>
                            <div className="home__banner-input w-[80%]">
                                <SearchIcon className='search-icon flex-end h-7 mx-5'/>
                                <div className="w-full text-center align-middle">
                                    <input className="w-[93%] focus:outline-none px-6 bg-transparent align-middle"
                                           type="text"/>
                                </div>
                            </div>

                        </div>
                        <CommCard/>
                        <div className="grid grid-rows-2 grid-flow-col">
                            <CommCard/>
                            <CommCard/>
                            <CommCard/>
                            <CommCard/>
                            <CommCard/>
                            <CommCard/>
                            <CommCard/>


                        </div>


                    </div>
                </div>


            </div>
        </>
    );
};

export default Homepage;