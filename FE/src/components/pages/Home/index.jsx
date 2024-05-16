import React from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

const Index = () => {
  return (
    <div className=" h-screen w-screen flex flex-col items-center justify-center">
      <div className=" h-full w-[70vw] py-4 px-4">
        <div className=" w-full h-fit flex flex-col">
          <h2 className=" font-bold">AI pulse creator</h2>
          <div className=" w-full h-full flex flex-row space-x-3 mt-2">
              <Input placeholder="Enter prompt" className=" outline-none"/>
              <Button>Create Pulse with AI</Button>
          </div>
        </div>

        <div>
          main pulses
        </div>


      </div>
    </div>
  );
};

export default Index;
