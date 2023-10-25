import './Filters.scss';
import settings from '../../assets/icons/settings.svg';
import professions from '../../utils/testProfessionArea.json';
import skillsData from '../../utils/testSkills.json';
import RadioGroupFilter from '../RadioGroupFilter/RadioGroupFilter';
import CheckboxGroupFilter from '../CheckboxGroupFilter/CheckboxGroupFilter';

function Filters() {
  return (
    <form className="filters">
      <div className="filters__header">
        <img className="filters__img" alt="settings" src={settings} />
        <h2 className="filters__title">Фильтры</h2>
      </div>
      <RadioGroupFilter
        panel="panel1"
        filter="profession"
        data={professions}
        withBorder={false}
      />
      <CheckboxGroupFilter
        filter="course"
        panel="panel2"
        title="Курс Практикума"
        data={professions}
      />
      <CheckboxGroupFilter
        filter="skills"
        panel="panel3"
        title="Навыки"
        placeholder="Введите навык"
        withSearch
        data={skillsData}
      />
      <CheckboxGroupFilter
        filter="experience"
        panel="panel4"
        title="Опыт работы"
        data={professions}
      />
      <CheckboxGroupFilter
        filter="level"
        panel="panel5"
        title="Уровень"
        data={professions}
      />
      <CheckboxGroupFilter
        filter="location"
        panel="panel6"
        title="Геопозиция"
        placeholder="Введите геопозицию"
        withSearch
        data={skillsData}
      />
      <CheckboxGroupFilter
        filter="busyType"
        panel="panel7"
        title="Тип занятости"
        data={professions}
      />
      <CheckboxGroupFilter
        filter="workingType"
        panel="panel8"
        title="График работы"
        data={professions}
      />
      <div className="filters__separator" />
    </form>
  );
}

export default Filters;
