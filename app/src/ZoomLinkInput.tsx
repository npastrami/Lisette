import React, { useState } from 'react';
import { Input, Button, XStack } from 'tamagui';

export const ZoomLinkInput = () => {
  const [link, setLink] = useState('');

  const handleJoin = () => {
    console.log("Joining Zoom Meeting:", link);
    // Here you will put the logic to command the bot to join the Zoom meeting.
  };

  return (
    <XStack>
      <Input
        value={link}
        onChange={(e: { target: { value: React.SetStateAction<string>; }; }) => setLink(e.target.value)}
        placeholder="Enter Zoom Link"
      />
      <Button onPress={handleJoin}>Join Meeting</Button>
    </XStack>
  );
};

export default ZoomLinkInput;