import React, { useEffect } from 'react';
import { BrowserRouter } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { QueryClient, QueryClientProvider } from 'react-query';
import { ReactQueryDevtools } from 'react-query/devtools';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

import Router from 'pages/router';
import { FallbackLoading } from 'components';
import { reAuthAsync } from 'state/user/authSlice';
import { AppDispatch } from 'state/store';

const App = () => {
  const queryClient = new QueryClient();
  const dispatch = useDispatch<AppDispatch>();
  const isDarkMode = document.documentElement.getAttribute('data-theme') === `dark` ? true : false;

  useEffect(() => {
    void dispatch(reAuthAsync());
  }, [dispatch]);

  return (
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <React.Suspense fallback={<FallbackLoading />}>
          <Router />
        </React.Suspense>
      </BrowserRouter>
      <ToastContainer
        position="bottom-right"
        autoClose={5000}
        hideProgressBar
        newestOnTop
        closeOnClick
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover
      />
      <ReactQueryDevtools initialIsOpen={false} />
    </QueryClientProvider>
  );
};

export default App;
