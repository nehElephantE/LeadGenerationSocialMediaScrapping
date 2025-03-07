import React from 'react';
import Header from "../Header/Header";
import './VerificationPage.css'
import {QuestionMarkCircleIcon, ReplyIcon, SearchIcon} from "@heroicons/react/outline";
import Button from "../UI/Button/Button";

const VerificationPage = () => {
    return (
        <>
            <Header/>
            <div className="verification-page-main flex-col ml-10">
                <div className="verification-page-heading">
                    Custom File Upload
                </div>
                <div className="flex content-center my-5">
                    <QuestionMarkCircleIcon className="h-8"/>
                    <div className="content-center my-auto verification-page-why ml-4">Why do we need to do
                        so?
                    </div>
                </div>

                <div className="flex content-center my-5">
                    <ReplyIcon className="h-12"/>
                    <div className="flex-col content-center verification-page-ans ml-4">Instructions & Short Description
                        about the circle Lorem ipsum dolor sit amet, consectetur adipiscing elit. In est dolor, tempus
                        nec augue nec, mattis venenatis mauris. Aliquam erat volutpat. Nam eget velit eget leo porta
                        facilisis. Vivamus bibendum diam lorem. Phasellus justo nisl, faucibus et neque vitae, auctor
                        ullamcorper dui. Fusce tempor tellus ipsum, id hendrerit justo
                    </div>
                </div>

                <div className="file-upload flex justify-between w-[40%]">
                    <input className="my-auto ml-5" type="file" name="upload" accept="application/pdf"/>
                    <div>
                        <Button>Submit</Button>
                    </div>
                </div>

            </div>

        </>
    );
};

export default VerificationPage;