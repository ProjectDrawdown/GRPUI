import React from "react"
import PropTypes from "prop-types"
import { Flex, Container } from "@chakra-ui/react"
import { PageFooter } from "parts/PageFooter"

const DashboardLayout = ({
  navMargin = true,
  maxW = "100%",
  showFooter = true,
  children
}) => {
  return (
    <Flex minH="100vh" direction="column" justifyContent="space-between">
      <Container
        top="0"
        pr="0"
        pl="1rem"
        pt="1rem"
        flex="1"
        maxW="none"
        position="fixed"
        ml={navMargin ? "3rem" : 0}
        mb="6rem"
        w={`calc(${maxW} - ${navMargin ? "3" : "0"}rem)`}
        h={showFooter ? `calc(${maxW} - 50px)` : maxW}
      >
        {children}
      </Container>
      {showFooter && <PageFooter px={8} py={4} />}
    </Flex>
  );
};

DashboardLayout.propTypes = {
  /** Enables margin */
  navMargin: PropTypes.bool,

  /** Max width of layout */
  maxW: PropTypes.string,

  /** enable/disable footer */
  showFooter: PropTypes.bool,

  children: PropTypes.elementType
}

export default DashboardLayout;
