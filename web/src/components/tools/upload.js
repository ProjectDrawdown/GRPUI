import React, { useState } from "react"
import { useLocation } from 'react-router-dom'
import { Image } from "@chakra-ui/react"

import { 
  Button, 
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalFooter,
  ModalBody,
  ModalCloseButton, 
  useDisclosure
} from "@chakra-ui/react";

import UploadIcon from 'images/icons/upload.svg'
import { uploadVMA } from "../../api/api";

const UploadResourceModal = ({ loading, onChangeHandler, name }) =>  {
  const { isOpen, onOpen, onClose } = useDisclosure();
  return (
    <>
      <Button colorScheme="orange" variant="solid" onClick={onOpen} title="Upload">
        <Image maxWidth="initial" src={UploadIcon} />
      </Button>
      <Modal isOpen={isOpen} onClose={onClose}>
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>Upload a new {name}</ModalHeader>
          <ModalCloseButton />
          <ModalBody>
            <input type="file" name="file" onChange={onChangeHandler} />
          </ModalBody>

          <ModalFooter>
            <Button colorScheme="blue" mr={3} onClick={onClose} isLoading={loading}>
              Close
            </Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </>
  )
}

function getTechFromURL(pathname) {
  const split = pathname.split('/')
  const tech = split[split.indexOf('technologies') + 1]

  return tech
}

export const UploadResource = ({ entity, name }) => {
  const [loading, setIsLoading] = useState(false);
  const [_,setIsFilePicked] = useState(false);

  const location = useLocation();
  const technology = getTechFromURL(location.pathname);

  const changeHandler = (event) => {
    setIsLoading(true);
    uploadFile(event.target.files[0]);
  };

  const uploadFile = async (file) => {
    const data = new FormData();
    data.append('file', file);
    data.append('name', file.name);
    const upload = await uploadVMA(data, entity, technology);
    // This is a hack, I dont like how we have to reload when new file is
    // uploaded, but its a way to repopulate the options
    window.location.reload();
  }

  return <UploadResourceModal onChangeHandler={changeHandler} name={name} loading={loading} />
}

