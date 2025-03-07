import React from 'react';
import Header from "../Header/Header";
import Card from "../UI/Card/Card";
import Profile from "../Profile/Profile";
import Banner from "../UI/Banner/Banner";
import {PaperAirplaneIcon, PaperClipIcon} from "@heroicons/react/outline";
import Chat from "../Chat/Chat";
import './PersonalChat.css';

const PersonalChat = () => {
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

                        </Card>
                    </div>
                    <div className="flex px-5 w-[100%]">

                        <Card className="card flex flex-col overflow-y-auto w-[100%] pb-6 h-[88vh]">

                            <div className="dm__profile mb-8 container">


                                <div className="text-center">
                                    <span className="profile__heading">Aloha</span>

                                </div>
                            </div>

                            <div
                                className="sticky top-5 bottom-20 chat__input-section flex items-center p-2.5 mx-8
                                    mb-4">

                                <PaperClipIcon className="h-10 mr-5 text-[#72767d]"/>

                                <div className="flex items-center chat__input w-full">
                                    <input type="text" placeholder="Search"
                                           className="focus:outline-none w-full bg-transparent p-4"

                                    />
                                    <button type="submit">
                                        <PaperAirplaneIcon className="h-10 text-[#72767d] mr-1 rotate-90"/>
                                    </button>

                                </div>
                            </div>

                        </Card>
                    </div>
                </div>


            </div>
        </>
    );
};

export default PersonalChat;