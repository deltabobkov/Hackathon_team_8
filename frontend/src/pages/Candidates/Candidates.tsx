import './Candidates.scss';
import Typography from '@mui/material/Typography';
import AppliedFilters from '../../components/AppliedFilters/AppliedFilters';
import VacanciesCards from '../../components/VacanciesCards/VacanciesCards';
import Filters from '../../components/Filters/Filters';

function Candidates() {
  return (
    <main className="candidates">
      <div>
        <Typography variant="h1">
          Кандидаты
        </Typography>
        <AppliedFilters />
        <VacanciesCards />
      </div>
      <Filters />
    </main>
  );
}

export default Candidates;
